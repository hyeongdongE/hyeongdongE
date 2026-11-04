# Profile Design Guide

## Concept

Minimal Technical Editorial Portfolio. 짧은 이름 중심 Hero, 한 문장 소개, 대표 작업 3개, 핵심 기술만 남긴 단일 열 구성입니다. 프로필은 빠른 탐색에 집중하고, 역할·구조·검증·한계는 기존 사례 문서에서 확인합니다.

## Color & Typography

| Token | Dark | Light |
| --- | --- | --- |
| Background | `#0D1117` | `#FFFFFF` |
| Text | `#E6EDF3` | `#17212F` |
| Secondary | `#919BA8` | `#586474` |
| Accent | `#65C6BE` | `#147D77` |
| Border | `#293440` | `#D8E1E8` |

본문은 GitHub 기본 폰트·제목 계층을 따릅니다. SVG는 Arial/Helvetica/system sans-serif 대체 글꼴을 사용하며 외부 폰트에 의존하지 않습니다. README 본문에는 커스텀 CSS를 넣지 않습니다.

## Image Standards

Hero viewBox는 720 × 180입니다. 기존 대비 높이를 약 59% 줄였습니다. 54px 이름, 24px 분야 요약과 작은 데이터 흐름 모티브만 사용합니다. SVG는 테마별 별도 파일, 로컬 경로, title/desc를 제공합니다. 스크립트·외부 리소스를 포함하지 않습니다. 테두리는 장식용이며 정보 전달을 맡기지 않습니다.

실제 화면은 출처와 촬영 조건을 확인한 뒤 추가합니다. 앱 디자인 시안은 동작 화면이나 운영 성과로 소개하지 않습니다. 이번 프로필에는 꾸며낸 UI 이미지를 추가하지 않았습니다.

## Section Responsibilities

- Introduction: 이름·분야를 Hero에서 보여주고 실제 텍스트 한 문장으로 하는 일을 설명합니다.
- Selected work: 프로젝트당 제목, 한 문장, 사례 링크. 제목은 저장소로 연결합니다. Supervisor의 Closed Beta 상태는 요약에 유지합니다.
- Stack: 공개 코드에서 확인한 핵심 기술만 두 줄로 정리합니다.
- 상세 역량·역할·구현 근거·제한사항·추가 확인 항목: 프로젝트 문서와 EVIDENCE.md에서 유지합니다. 미확인 프로젝트는 프로필 첫 화면에 노출하지 않습니다.

## Add a Project

1. 공개 저장소와 기준 커밋을 확인합니다.
2. `docs/projects/`에 Overview, Problem, My Role, System Architecture, Implementation, Verification, Results, Lessons Learned를 작성합니다.
3. 역할은 커밋·작업 기록과 연결하고, 기능은 실제 실행 진입점에서 확인합니다.
4. README는 프로젝트당 한 문장과 사례 링크만 넣습니다. 세부 역할·기술·통계는 사례 문서에 적고 근거를 연결합니다.
5. 상대 링크, 테마별 Hero, 390px·1440px 화면을 다시 확인합니다.

## Maintenance

프로젝트의 실행 경로가 바뀌면 사례 문서와 README를 함께 갱신합니다. Closed Beta 표기는 공식 상태 변경을 확인한 뒤 수정합니다. `EVIDENCE.md`의 기준 커밋과 검증 날짜를 갱신합니다. MQTT·IoT 등은 본인 구현 자료를 확보한 후 기술 목록에 추가합니다.

기업연계 자료는 외부 공개 허용이 확인된 비식별 설명만 사용합니다. 원문 내부 문서나 데이터는 이 저장소에 복사하지 않습니다.

## GitHub Manual Settings

프로필 표시 조건: 사용자명과 같은 이름의 **Public** 저장소 `hyeongdongE/hyeongdongE`, 루트의 비어 있지 않은 `README.md`.

추천 고정 순서: `ai-supervisor` → `ai-mvp-orchestrator` → `peakrew` → `ai-app-template`. GitHub 프로필의 Customize your pins에서 수동 설정합니다. AI App Template은 Orchestrator의 실행 스크립트와 mock/API 경계 근거로 사용합니다.

Bio 제안: `AI Transformation · AI Agent Systems · Backend Engineering | 검증 가능한 업무 자동화`

프로필 Bio와 Pins는 이번 저장소 작업에서 변경하지 않았습니다.
