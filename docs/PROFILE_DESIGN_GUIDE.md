# Profile Design Guide

## Concept

AI가 다 했다고 말하면 증거로 확인한다는 한 문장에서 출발합니다. 히어로는 요청, Agent 실행, 직접 검증, 되돌림, 판정의 실제 흐름을 한 번 움직여 보여주고, 프로젝트는 왼쪽에 하는 일, 오른쪽에 근거를 둔 판정 전표로 나열합니다. 점선은 주장과 근거의 경계를 뜻합니다.

## Color & Typography

| Token | Dark | Light |
| --- | --- | --- |
| Hero 배경 | `#3B2D28` | `#3B2D28` |
| 전표 배경 | `#2B211E` | `#EFEDF1` |
| Text | `#F1EDEE` | `#2B201C` |
| Secondary | `#C9BFBD` | `#5E514C` |
| Accent | `#D3CAF7` | `#5A4AA6` |

모카, 플래티넘, 라벤더는 Voruvi의 색을 이어받습니다. 제목과 근거 숫자는 Hahmlet Bold, 나머지는 IBM Plex Sans KR입니다. 글자는 경로로 변환해 기기 글꼴에 영향받지 않습니다.

## Image Standards

`assets/`의 SVG는 `scripts/build_assets.py`로 만듭니다. 글자가 경로이므로 직접 수정하지 말고 스크립트의 문구를 고쳐 다시 생성합니다. viewBox 폭은 720이고 글자는 20 이상으로 둡니다. 390px 화면에서도 10px 이상으로 읽히는 크기입니다. 히어로 애니메이션은 한 번만 재생되고 끝난 상태로 멈추며, 동작 줄이기 설정에서는 최종 상태만 보여줍니다. 스크립트와 외부 리소스는 넣지 않습니다.

실제 화면은 출처와 촬영 조건을 확인한 뒤 추가합니다. 앱 디자인 시안은 동작 화면이나 운영 성과로 소개하지 않습니다.

## Section Responsibilities

- Hero: 직무와 일하는 방식을 보여줍니다.
- 소개: 실제 텍스트 두 문장으로 검색과 스크린리더를 지원합니다.
- 대표 프로젝트: 전표 하나와 접히는 코드 근거 하나. 전표의 상태 표기는 실제 단계와 일치해야 합니다.
- 사용 기술: 공개 코드에서 확인한 항목만 적습니다.
- 상세 역할, 구현 근거, 제한사항은 프로젝트 문서와 EVIDENCE.md에 둡니다. 미확인 프로젝트는 프로필 첫 화면에 노출하지 않습니다.

## Add a Project

1. 공개 저장소와 기준 커밋을 확인합니다.
2. `docs/projects/`에 Overview, Problem, My Role, System Architecture, Implementation, Verification, Results, Lessons Learned를 작성합니다.
3. 역할은 커밋·작업 기록과 연결하고, 기능은 실제 실행 진입점에서 확인합니다.
4. `scripts/build_assets.py`의 `SLIPS`에 전표를 추가하고, README에 전표와 코드 근거를 넣습니다. 세부 역할·기술·통계는 사례 문서에 적습니다.
5. 상대 링크, 테마별 Hero, 390px·1440px 화면을 다시 확인합니다.

## Maintenance

프로젝트의 실행 경로가 바뀌면 사례 문서와 README를 함께 갱신합니다. Closed Beta 표기는 공식 상태 변경을 확인한 뒤 수정합니다. `EVIDENCE.md`의 기준 커밋과 검증 날짜를 갱신합니다. MQTT·IoT 등은 본인 구현 자료를 확보한 후 기술 목록에 추가합니다.

기업연계 자료는 외부 공개 허용이 확인된 비식별 설명만 사용합니다. 원문 내부 문서나 데이터는 이 저장소에 복사하지 않습니다.

## GitHub Manual Settings

프로필 표시 조건: 사용자명과 같은 이름의 **Public** 저장소 `hyeongdongE/hyeongdongE`, 루트의 비어 있지 않은 `README.md`.

추천 고정 순서: `ai-supervisor` → `mzapp` → `ai-mvp-orchestrator` → `peakrew`. GitHub 프로필의 Customize your pins에서 수동 설정합니다. AI App Template은 Orchestrator 근거에서 링크합니다.

Bio 제안: `AX 개발자. AI Agent가 일하게 만들고, 결과는 증거로 확인합니다.`

프로필 Bio와 Pins는 이번 저장소 작업에서 변경하지 않았습니다.
