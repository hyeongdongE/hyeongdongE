#!/usr/bin/env python3
"""프로필 SVG를 다시 만듭니다. 글자는 경로로 변환되어 기기 글꼴과 무관하게 같은 모양으로 보입니다.

준비:
  pip install fonttools brotli
  npm pack @fontsource/hahmlet @fontsource/ibm-plex-sans-kr  (각각 압축 해제)
실행:
  HAHMLET_DIR=.../hahmlet/package/files PLEX_DIR=.../plex/package/files python3 scripts/build_assets.py
글꼴 파일은 저장소에 넣지 않습니다. 두 글꼴 모두 SIL Open Font License입니다.
"""
import glob
import os
from html import escape
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

OUT = Path(__file__).resolve().parent.parent / "assets"

MOCHA = "#3B2D28"
THEMES = {
    "dark": dict(bg="#2B211E", ink="#F1EDEE", soft="#C9BFBD", accent="#D3CAF7", rule="#6E5D57"),
    "light": dict(bg="#EFEDF1", ink="#2B201C", soft="#5E514C", accent="#5A4AA6", rule="#A79DA3"),
}


def fmt(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s in ("", "-0") else s


class Face:
    def __init__(self, directory, family_weight):
        self.map = {}
        for path in sorted(glob.glob(f"{directory}/*-{family_weight}-normal.woff2")):
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


SERIF = Face(os.environ["HAHMLET_DIR"], 700)
SANS = Face(os.environ["PLEX_DIR"], 400)
SANS_M = Face(os.environ["PLEX_DIR"], 500)


def text(face, s, x, y, size, fill, anchor="start", tracking=0, cls=""):
    if anchor == "end":
        x -= face.width(s, size, tracking)
    elif anchor == "middle":
        x -= face.width(s, size, tracking) / 2
    c = f' class="{cls}"' if cls else ""
    return f'<path{c} fill="{fill}" d="{face.path(s, x, y, size, tracking)}"/>'


def head(w, h, title, desc):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">'
        f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>'
    )


def hero():
    ink, soft, lav, dim = "#F4F0F0", "#CFC5C3", "#D3CAF7", "#7A6961"
    W, H, Y = 720, 392, 308
    xs = [52, 255, 458, 661]
    arc = f"M{xs[2]} {Y-13}C{xs[2]-18} {Y-74} {xs[1]+18} {Y-74} {xs[1]+6} {Y-16}"
    parts = [
        head(W, H, "이형동, AX 개발자",
             "AI가 다 했다고 말하면, 증거로 확인합니다. 요청, Agent 실행, 직접 검증을 거치고 "
             "어긋나면 되돌려 다시 실행한 뒤 판정하는 흐름도."),
        """<style>
.d{stroke-dasharray:1;animation:draw var(--t) ease-in-out var(--w) both}
.n{animation:pop .3s ease-out var(--w) both;transform-box:fill-box;transform-origin:center}
.l{animation:lit .3s linear var(--w) both}
@keyframes draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes pop{from{opacity:0;transform:scale(.4)}to{opacity:1;transform:scale(1)}}
@keyframes lit{from{opacity:.45}to{opacity:1}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>""",
        f'<rect width="{W}" height="{H}" rx="18" fill="{MOCHA}"/>',
        text(SANS_M, "AX 개발자 이형동", 43, 62, 23, soft),
        text(SERIF, "AI가 다 했다고 말하면,", 42, 124, 47, ink, tracking=-0.8),
        text(SERIF, "증거로 확인합니다", 42, 184, 47, ink, tracking=-0.8),
        # 바닥 선과 되돌림 호
        f'<path d="M{xs[0]} {Y}H{xs[3]}" stroke="{dim}" stroke-width="2.5" fill="none"/>',
        f'<path d="{arc}" stroke="{dim}" stroke-width="2.5" stroke-dasharray="2 7" stroke-linecap="round" fill="none"/>',
        # 움직이는 선: 검증까지 갔다가, 되돌아가고, 판정으로 나아갑니다
        f'<path class="d" style="--t:1.2s;--w:.5s" pathLength="1" d="M{xs[0]} {Y}H{xs[2]}" stroke="{lav}" stroke-width="3" fill="none"/>',
        f'<path class="d" style="--t:.8s;--w:1.75s" pathLength="1" d="{arc}" stroke="{lav}" stroke-width="3" stroke-linecap="round" fill="none"/>',
        f'<path class="d" style="--t:.6s;--w:2.7s" pathLength="1" d="M{xs[2]} {Y}H{xs[3]}" stroke="{lav}" stroke-width="3" fill="none"/>',
        # 호 끝 화살촉
        f'<path class="n" style="--w:2.45s" d="M{xs[1]-3} {Y-27}l8 12 9-11" stroke="{lav}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
        text(SANS, "어긋나면 되돌려 다시", (xs[1] + xs[2]) / 2, Y - 66, 20, soft, "middle"),
    ]
    delays = [0.3, 0.95, 1.6, 3.2]
    for x, w in zip(xs[:3], delays):
        parts.append(f'<circle cx="{x}" cy="{Y}" r="10" fill="{MOCHA}" stroke="{dim}" stroke-width="2.5"/>')
        parts.append(f'<circle class="n" style="--w:{w}s" cx="{x}" cy="{Y}" r="10" fill="{lav}"/>')
    x = xs[3]
    parts.append(f'<circle class="n" style="--w:{delays[3]}s" cx="{x}" cy="{Y}" r="17" fill="{lav}"/>')
    parts.append(f'<path class="d" style="--t:.35s;--w:3.4s" pathLength="1" d="M{x-8} {Y+1}l6 6 11-13" stroke="{MOCHA}" stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    labels = [("요청", "start", 42), ("Agent 실행", "middle", xs[1]), ("직접 검증", "middle", xs[2]), ("판정", "end", 678)]
    for (s, a, lx), w in zip(labels, delays):
        parts.append(f'<g class="l" style="--w:{w}s">{text(SANS_M, s, lx, Y + 52, 22, ink, a)}</g>')
    parts.append("</svg>")
    return "".join(parts)


SLIPS = {
    "voruvi": dict(
        name="Voruvi", state="개발 중, 구 AI Supervisor",
        lines=["Codex와 Claude Code를 한 팀으로 실행하고,", "끝나면 결과를 직접 검사합니다."],
        proof="5단계", note=["Agent를 일에 넣기 전", "실제로 돌려 보는 검증"],
    ),
    "solopilot": dict(
        name="SoloPilot", state="공개 전",
        lines=["흩어진 IT 소식을 근거가 붙은", "5분 이내 브리핑으로 만듭니다."],
        proof="0 / 14", note=["근거 없는 주장 수,", "기록 데이터 평가 기준"],
    ),
    "orchestrator": dict(
        name="AI MVP Orchestrator", state="프론트 승인까지 구현",
        lines=["기획부터 화면 구현, 스크린샷 승인", "요청까지 자동으로 잇습니다."],
        proof="사람 승인", note=["자동화가 끝나는 지점을", "코드로 명시한 경계"],
    ),
    "peakrew": dict(
        name="Peakrew", state="공공 데이터 파이프라인",
        lines=["공공 데이터 8종을 공통 모델로 정리하고,", "발행 여부와 이유를 규칙으로 남깁니다."],
        proof="25개 통과", note=["수집기 테스트,", "2026년 11월 직접 실행"],
    ),
}


def slip(key, s, theme):
    t = THEMES[theme]
    W, H, D, r, n = 720, 196, 478, 14, 11
    shape = (
        f"M{r} 0H{D-n}A{n} {n} 0 0 0 {D+n} 0H{W-r}A{r} {r} 0 0 1 {W} {r}V{H-r}A{r} {r} 0 0 1 {W-r} {H}"
        f"H{D+n}A{n} {n} 0 0 0 {D-n} {H}H{r}A{r} {r} 0 0 1 0 {H-r}V{r}A{r} {r} 0 0 1 {r} 0Z"
    )
    desc = f"{s['state']}. {' '.join(s['lines'])} 근거: {s['proof']}, {' '.join(s['note'])}"
    name_size = 29 if len(s["name"]) > 12 else 34
    parts = [
        head(W, H, s["name"], desc),
        f'<path d="{shape}" fill="{t["bg"]}"/>',
        f'<path d="M{D} {n+9}V{H-n-9}" stroke="{t["rule"]}" stroke-width="2" stroke-dasharray="0.1 9" stroke-linecap="round"/>',
        text(SERIF, s["name"], 30, 56, name_size, t["ink"], tracking=-0.3),
        text(SANS, s["state"], 31, 90, 20, t["soft"]),
        text(SANS, s["lines"][0], 31, 134, 22, t["ink"]),
        text(SANS, s["lines"][1], 31, 165, 22, t["ink"]),
        text(SERIF, s["proof"], 508, 92, 43, t["accent"], tracking=-0.5),
        text(SANS, s["note"][0], 509, 132, 20, t["soft"]),
        text(SANS, s["note"][1], 509, 160, 20, t["soft"]),
        "</svg>",
    ]
    return "".join(parts)


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "hero.svg").write_text(hero(), encoding="utf-8")
    for key, s in SLIPS.items():
        for theme in THEMES:
            (OUT / f"{key}-{theme}.svg").write_text(slip(key, s, theme), encoding="utf-8")
    for p in sorted(OUT.glob("*.svg")):
        print(p.name, p.stat().st_size)


if __name__ == "__main__":
    main()
