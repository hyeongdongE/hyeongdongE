# Evidence & Publication Notes

조사 기준: 2026-11-04. 공개 저장소·공개 Release와 사용자 제공 내용만 사용했습니다. 비공개 저장소는 조사하거나 복사하지 않았습니다.

## Source Baseline

| Repository | Reviewed commit |
| --- | --- |
| [ai-supervisor](https://github.com/hyeongdongE/ai-supervisor/tree/f4746a9d2b762f1c173f34afc19fdba766964fbf) | `f4746a9d2b762f1c173f34afc19fdba766964fbf` |
| [ai-mvp-orchestrator](https://github.com/hyeongdongE/ai-mvp-orchestrator/tree/003c3470c28874de2a1dd13d694001e643fc29e4) | `003c3470c28874de2a1dd13d694001e643fc29e4` |
| [ai-app-template](https://github.com/hyeongdongE/ai-app-template/tree/674e27e013222568c0a9891c74771363d887bf6b) | `674e27e013222568c0a9891c74771363d887bf6b` |
| [peakrew](https://github.com/hyeongdongE/peakrew/tree/35be5688bc5af68b8c5b1eb035184653542bdff7) | `35be5688bc5af68b8c5b1eb035184653542bdff7` |
| [mzapp (SoloPilot)](https://github.com/hyeongdongE/mzapp/tree/ebacc3f89784251e31f6c27876b6dd708da4fd5b) | `ebacc3f89784251e31f6c27876b6dd708da4fd5b` |

## Claim Boundaries

- Supervisor: 공개 Git에는 README만 존재. 공개 wheel Python 코드를 정적 검토했습니다. 정식 출시·실행 성공률·완전한 보안 격리로 확대 해석하지 않습니다.
- Orchestrator: README보다 최신 Runner의 frontend-only 종료 동작을 우선했습니다. 전체 배포 자동화 완료로 소개하지 않습니다.
- Peakrew: 공통 모델·해시·증분 상태·발행 게이트 구현과 공개 테스트를 확인했습니다. 기관 간 의미적 중복 제거·실서비스 정확도와 구분합니다.
- Orchestrator·Template·Peakrew는 공개 contributors에서 계정 기여를 확인했습니다. 기능별 단독 담당 범위는 추가 확인이 필요합니다.
- Voruvi는 AI Supervisor의 새 이름입니다(사용자 확인). 코드 근거는 공개 배포본 `0.1.0b1`에 한정하며, 개발 중인 Voruvi 앱의 코드는 검토하지 않았습니다.
- SoloPilot: 평가 수치는 저장소 기록(2026-09-23, 기준 커밋 `a229c14`)을 인용했으며 다시 실행하지 않았습니다. 실제 LLM은 비활성이고 사용자 공개 전입니다.
- Supervisor의 세부 역할, 기업연계 기간·역할, AIoT 세부 구현, SSAFY 기간, 수상명·등급, FLY ASIA 전시명·연도는 확인하지 못했습니다.
- Smart Fish Tank 팀장과 기업연계 경험은 사용자 제공 정보로 명시했습니다. 정식 회사 재직으로 표현하지 않습니다.
- SQL은 Peakrew SQLite 상태 저장 SQL, TypeScript는 Peakrew·Template 프론트, Java/Spring/MySQL/Docker는 빌드·코드·구성 파일에서 확인했습니다. MQTT는 근거가 없어 기술 목록에서 제외했습니다.

## Validation

- Peakrew 기존 테스트: 격리 venv, Python 3.12.14, `PYTHONPATH=crawler python -m pytest -q -p no:cacheprovider crawler/tests` → **25 passed**. API 키·실시간 API 호출을 사용하지 않았습니다.
- GitHub Markdown API: README를 GFM HTML로 렌더링했습니다.
- 내부 파일 링크·이미지 경로 검사 통과. 공개 외부 URL 16개에서 HTTP 200을 확인했습니다. 섹션 fragment는 별도 제목과 대조했습니다.
- Hero 2개 XML 파싱 통과. 스크립트·외부 리소스 없음. 배경 대비 주·보조·강조 텍스트 모두 4.5:1 이상입니다.
- Chromium 로컬 미리보기: GitHub Markdown API HTML + 공개 github-markdown-css를 사용했습니다. 실제 GitHub 페이지와 완전히 동일한 레이아웃을 보증하지는 않습니다.
- 390px·1440px × dark·light 네 조합의 전체 스크린샷을 직접 확인했습니다. 가로 넘침 없음, 이미지 로드·테마별 Hero 전환 정상. 모바일 제목에서 한글 이름이 어색하게 줄바꿈되어 제목과 소개 행으로 분리했습니다.
- 최초 저장소 생성은 `createRepository` 권한 오류로 차단되었으나, 사용자가 빈 Public 저장소를 생성한 뒤 2026-11-04 `main` push에 성공했습니다. API에서 Public·기본 브랜치 `main`·루트 README 및 assets/docs 존재를 확인했습니다.
- 타 프로젝트의 소스코드는 수정하지 않았습니다. 프레임워크·빌드 의존성을 프로필 저장소에 추가하지 않았습니다.

## Live GitHub Profile Check

2026-11-04 공개 반영 후 확인.

- Chromium으로 실제 `https://github.com/hyeongdongE`를 390px·1440px × light·dark 네 조합으로 열었습니다. 네 응답 모두 HTTP 200입니다.
- 프로필 README가 표시되고, 두 테마의 Hero가 각 로컬 자산 URL에서 정상 로드되는 것을 확인했습니다.
- 네 조합 모두 가로 넘침이 없었으며, 전체 스크린샷을 직접 확인했습니다.
- 대표 사례 문서 3개는 실제 GitHub에서 HTTP 200을 반환했고, Mermaid 아키텍처의 렌더링과 화면을 확인했습니다. Supervisor는 초기 로딩 이후 노드 텍스트가 나타날 때까지 기다려 재확인했습니다.

## Compact Design Revision

- 사용자 요청에 따라 README를 소개 한 문장·대표 작업 3개·기술 두 줄로 축약했습니다. 긴 설명과 검증 기록은 기존 사례 문서에 보존했습니다.
- Hero를 720 × 440에서 720 × 180으로 줄이고, 이름과 분야·작은 흐름 모티브로 재설계했습니다.
- GitHub Markdown API 렌더링, 내부 파일 링크, 두 SVG의 XML·외부 리소스 부재와 `git diff --check`를 확인했습니다.
- 로컬 Chromium에서 390px·1440px × light·dark 네 화면을 직접 확인했습니다. Hero 이미지 로드·테마 전환·가로 넘침 검사 통과.

## AX Proof Revision

2026-11-04, 프로필을 AX 역량 증명 구조로 개편했습니다.

| 프로필 표시 | 확인 방법 |
| --- | --- |
| Voruvi 5 checks | wheel SHA-256 일치 확인 후 `registry/verify.py`의 `static`, `isolation`, `permission`, `capability`, `capability_proof`를 코드에서 확인 |
| SoloPilot 0 / 14 | [품질 평가 기록](https://github.com/hyeongdongE/mzapp/blob/ebacc3f89784251e31f6c27876b6dd708da4fd5b/docs/it-intelligence/quality-evaluation.md)의 기록 데이터 E2E 수치 인용. 이번에 다시 실행하지 않음 |
| Orchestrator human gate | `OrchestrationRunner`의 승인 생성과 Discord 요청, 승인 후 종료 경계를 코드에서 확인 |
| Peakrew 25 passed | Python 3.12 격리 환경에서 `crawler/tests` 직접 실행, 25 passed. API 키와 실시간 호출 없음 |
| Peakrew 공공 데이터 8종 | `crawler/opportunity_crawler/adapters`의 어댑터 8개. 같은 기관의 API가 포함되어 있어 기관 수가 아님 |

- 히어로의 로그는 작동 흐름 예시이며 실제 실행 기록이 아닙니다.
- 사용 기술은 각 저장소의 빌드 파일, `package.json`, Compose 파일, 워크플로에서 확인한 항목만 적었습니다.
- 비공개 저장소의 이름과 내용은 프로필에 쓰지 않았습니다.
