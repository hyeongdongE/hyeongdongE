# Evidence & Publication Notes

조사 기준: 2026-11-04. 공개 저장소·공개 Release와 사용자 제공 내용만 사용했습니다. 비공개 저장소는 조사하거나 복사하지 않았습니다.

## Source Baseline

| Repository | Reviewed commit |
| --- | --- |
| [ai-supervisor](https://github.com/hyeongdongE/ai-supervisor/tree/f4746a9d2b762f1c173f34afc19fdba766964fbf) | `f4746a9d2b762f1c173f34afc19fdba766964fbf` |
| [ai-mvp-orchestrator](https://github.com/hyeongdongE/ai-mvp-orchestrator/tree/003c3470c28874de2a1dd13d694001e643fc29e4) | `003c3470c28874de2a1dd13d694001e643fc29e4` |
| [ai-app-template](https://github.com/hyeongdongE/ai-app-template/tree/674e27e013222568c0a9891c74771363d887bf6b) | `674e27e013222568c0a9891c74771363d887bf6b` |
| [peakrew](https://github.com/hyeongdongE/peakrew/tree/35be5688bc5af68b8c5b1eb035184653542bdff7) | `35be5688bc5af68b8c5b1eb035184653542bdff7` |

## Claim Boundaries

- Supervisor: 공개 Git에는 README만 존재. 공개 wheel Python 코드를 정적 검토했습니다. 정식 출시·실행 성공률·완전한 보안 격리로 확대 해석하지 않습니다.
- Orchestrator: README보다 최신 Runner의 frontend-only 종료 동작을 우선했습니다. 전체 배포 자동화 완료로 소개하지 않습니다.
- Peakrew: 공통 모델·해시·증분 상태·발행 게이트 구현과 공개 테스트를 확인했습니다. 기관 간 의미적 중복 제거·실서비스 정확도와 구분합니다.
- Orchestrator·Template·Peakrew는 공개 contributors에서 계정 기여를 확인했습니다. 기능별 단독 담당 범위는 추가 확인이 필요합니다.
- Supervisor의 세부 역할, Voruvi 관계, 기업연계 기간·역할, AIoT 세부 구현, SSAFY 기간, 수상명·등급, FLY ASIA 전시명·연도는 확인하지 못했습니다.
- Smart Fish Tank 팀장과 기업연계 경험은 사용자 제공 정보로 명시했습니다. 정식 회사 재직으로 표현하지 않습니다.
- SQL은 Peakrew SQLite 상태 저장 SQL, TypeScript는 Peakrew·Template 프론트, Java/Spring/MySQL/Docker는 빌드·코드·구성 파일에서 확인했습니다. MQTT는 근거가 없어 기술 목록에서 제외했습니다.

## Validation

- Peakrew 기존 테스트: 격리 venv, Python 3.12.14, `PYTHONPATH=crawler python -m pytest -q -p no:cacheprovider crawler/tests` → **25 passed**. API 키·실시간 API 호출을 사용하지 않았습니다.
- GitHub Markdown API: README를 GFM HTML로 렌더링했습니다.
- 내부 파일 링크·이미지 경로 검사 통과. 공개 외부 URL 16개에서 HTTP 200을 확인했습니다. 섹션 fragment는 별도 제목과 대조했습니다.
- Hero 2개 XML 파싱 통과. 스크립트·외부 리소스 없음. 배경 대비 주·보조·강조 텍스트 모두 4.5:1 이상입니다.
- Chromium 로컬 미리보기: GitHub Markdown API HTML + 공개 github-markdown-css를 사용했습니다. 실제 GitHub 페이지와 완전히 동일한 레이아웃을 보증하지는 않습니다.
- 390px·1440px × dark·light 네 조합의 전체 스크린샷을 직접 확인했습니다. 가로 넘침 없음, 이미지 로드·테마별 Hero 전환 정상. 모바일 제목에서 한글 이름이 어색하게 줄바꿈되어 제목과 소개 행으로 분리했습니다.
- 원격 저장소 생성은 GitHub의 `Resource not accessible by integration (createRepository)` 오류로 차단되었습니다. 로컬 이름·README 조건은 충족하지만 실제 프로필 표시와 GitHub 페이지의 테마별 시각 검증은 완료하지 못했습니다.
- 타 프로젝트의 소스코드는 수정하지 않았습니다. 프레임워크·빌드 의존성을 프로필 저장소에 추가하지 않았습니다.
