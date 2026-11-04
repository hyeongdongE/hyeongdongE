#!/usr/bin/env python3
"""프로필 SVG를 다시 만듭니다. 글자는 경로로 변환되어 기기 글꼴과 무관하게 같은 모양으로 보입니다.

준비:
  pip install fonttools brotli
  npm pack @fontsource/geist-sans @fontsource/geist-mono pretendard  (각각 압축 해제)
실행:
  GEIST_DIR=.../geist-sans/package/files GEIST_MONO_DIR=.../geist-mono/package/files \\
  PRETENDARD_DIR=.../pretendard/package/dist/web/static/woff2 python3 scripts/build_assets.py
글꼴 파일은 저장소에 넣지 않습니다. 세 글꼴 모두 SIL Open Font License입니다.
"""
import os
from html import escape
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

OUT = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark": dict(ink="#FFFFFF", soft="#A3A3A3", rule="#2E2E2E"),
    "light": dict(ink="#000000", soft="#595959", rule="#E0E0E0"),
}


def fmt(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s in ("", "-0") else s


class Face:
    def __init__(self, *paths):
        self.map = {}
        for path in paths:
            font = TTFont(path, lazy=True)
            for cp in font.getBestCmap():
                self.map.setdefault(cp, path)
        self.open = {}

    def font(self, cp):
        if cp not in self.map:
            raise KeyError(f"글리프 없음: {chr(cp)!r}")
        path = self.map[cp]
        if path not in self.open:
            font = TTFont(path)
            self.open[path] = (font, font.getGlyphSet(), font.getBestCmap(), font["head"].unitsPerEm)
        return self.open[path]

    def advance(self, ch, size):
        font, gs, cmap, upem = self.font(ord(ch))
        return gs[cmap[ord(ch)]].width * size / upem

    def width(self, text, size, tracking=0):
        return sum(self.advance(c, size) + tracking for c in text) - tracking

    def path(self, text, x, y, size, tracking=0):
        out = []
        for ch in text:
            font, gs, cmap, upem = self.font(ord(ch))
            glyph = gs[cmap[ord(ch)]]
            scale = size / upem
            pen = SVGPathPen(gs, ntos=fmt)
            glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
            out.append(pen.getCommands())
            x += glyph.width * scale + tracking
        return "".join(out)


def text(face, s, x, y, size, fill, anchor="start", tracking=0, cls=""):
    if anchor == "end":
        x -= face.width(s, size, tracking)
    elif anchor == "middle":
        x -= face.width(s, size, tracking) / 2
    c = f' class="{cls}"' if cls else ""
    return f'<path{c} fill="{fill}" d="{face.path(s, x, y, size, tracking)}"/>'


GEIST = Face(f"{os.environ['GEIST_DIR']}/geist-sans-latin-600-normal.woff2")
MONO = Face(f"{os.environ['GEIST_MONO_DIR']}/geist-mono-latin-400-normal.woff2")
MONO_M = Face(f"{os.environ['GEIST_MONO_DIR']}/geist-mono-latin-500-normal.woff2")
KR = Face(f"{os.environ['PRETENDARD_DIR']}/Pretendard-Regular.woff2")
KR_M = Face(f"{os.environ['PRETENDARD_DIR']}/Pretendard-Medium.woff2")


def head(w, h, title, desc):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">'
        f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>'
    )


LOG = [
    ("agent", 'reports "done"'),
    ("verify", "runs the tests itself"),
    ("verify", "mismatch, rewinds the step"),
    ("agent", "reworks the step"),
    ("verify", "passes, verdict recorded"),
]


def hero():
    W, H, X = 720, 414, 40
    parts = [
        head(W, H, "이형동, AX Engineer",
             "AI가 다 했다고 말하면, 증거로 확인합니다. 작동 흐름 예시: Agent가 완료를 보고하면 "
             "테스트를 직접 실행하고, 어긋나면 되돌려 다시 작업시킨 뒤 통과하면 판정을 기록합니다."),
        """<style>
.s{animation:s .14s linear var(--w) both}
.c{animation:b 1s steps(1,end) 2.9s 3 both}
@keyframes s{from{opacity:0}to{opacity:1}}
@keyframes b{0%{opacity:1}50%{opacity:0}100%{opacity:1}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>""",
        f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="10" fill="#000" stroke="#2E2E2E"/>',
        text(KR_M, "이형동", X, 62, 22, "#A3A3A3"),
        text(GEIST, "AX Engineer", X - 3, 124, 62, "#FFF", tracking=-2.6),
        text(KR_M, "AI가 다 했다고 말하면, 증거로 확인합니다", X, 170, 25, "#D4D4D4", tracking=-0.2),
        f'<path d="M{X} 200.5H{W-X}" stroke="#2E2E2E"/>',
    ]
    y, step = 240, 32
    for i, (who, what) in enumerate(LOG):
        last = i == len(LOG) - 1
        left = "#FFF" if last else "#737373"
        right = "#FFF" if last else "#A3A3A3"
        parts.append(
            f'<g class="s" style="--w:{.5 + i * .5}s">'
            f'{text(MONO, who, X, y + i * step, 21, left)}'
            f'{text(MONO_M if last else MONO, what, X + 104, y + i * step, 21, right)}</g>'
        )
    cx = X + 104 + MONO_M.width(LOG[-1][1], 21) + 10
    cy = y + (len(LOG) - 1) * step
    parts.append(f'<g class="s" style="--w:2.5s"><rect class="c" x="{fmt(cx)}" y="{cy-17}" width="12" height="22" fill="#FFF"/></g>')
    parts.append("</svg>")
    return "".join(parts)


ROWS = {
    "voruvi": dict(
        name="Voruvi", state="개발 중, 구 AI Supervisor",
        lines=["Codex와 Claude Code를 한 팀으로 실행하고,", "끝나면 결과를 직접 검사합니다."],
        proof="5 checks", note="Agent 사전 검증",
    ),
    "solopilot": dict(
        name="SoloPilot", state="공개 전",
        lines=["흩어진 IT 소식을 근거가 붙은", "5분 이내 브리핑으로 만듭니다."],
        proof="0 / 14", note="근거 없는 주장, 기록 평가 기준",
    ),
    "orchestrator": dict(
        name="AI MVP Orchestrator", state="프론트 승인까지 구현",
        lines=["기획부터 화면 구현, 스크린샷 승인", "요청까지 자동으로 잇습니다."],
        proof="human gate", note="자동화가 멈추는 승인 경계",
    ),
    "peakrew": dict(
        name="Peakrew", state="공공 데이터 파이프라인",
        lines=["공공 데이터 8종을 공통 모델로 정리하고,", "발행 여부와 이유를 규칙으로 남깁니다."],
        proof="25 passed", note="수집기 테스트 직접 실행",
    ),
}


def row(key, s, theme, first, last):
    t = THEMES[theme]
    W, H = 720, 150
    desc = f"{s['state']}. {' '.join(s['lines'])} 근거: {s['proof']}, {s['note']}"
    x = GEIST.width(s["name"], 28, -0.5) + 14
    parts = [
        head(W, H, s["name"], desc),
        text(GEIST, s["name"], 0, 50, 28, t["ink"], tracking=-0.5),
        text(KR, s["state"], x, 50, 20, t["soft"]),
        text(KR, s["lines"][0], 0, 92, 22, t["soft"]),
        text(KR, s["lines"][1], 0, 124, 22, t["soft"]),
        text(MONO_M, s["proof"], W, 50, 29, t["ink"], "end", tracking=-0.6),
        text(KR, s["note"], W, 92, 20, t["soft"], "end"),
    ]
    if not first:
        parts.insert(1, f'<path d="M0 .5H{W}" stroke="{t["rule"]}"/>')
    if last:
        parts.append(f'<path d="M0 {H-.5}H{W}" stroke="{t["rule"]}"/>')
    parts.append("</svg>")
    return "".join(parts)


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "hero.svg").write_text(hero(), encoding="utf-8")
    keys = list(ROWS)
    for key, s in ROWS.items():
        for theme in THEMES:
            svg = row(key, s, theme, key == keys[0], key == keys[-1])
            (OUT / f"{key}-{theme}.svg").write_text(svg, encoding="utf-8")
    for p in sorted(OUT.glob("*.svg")):
        print(p.name, p.stat().st_size)


if __name__ == "__main__":
    main()
