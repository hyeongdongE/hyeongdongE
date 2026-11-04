<p><img src="assets/hero.svg" width="100%" alt="AX 개발자 이형동. AI가 다 했다고 말하면, 증거로 확인합니다. 요청, Agent 실행, 직접 검증을 거치고, 어긋나면 되돌려 다시 실행한 뒤 판정합니다."></p>

업무를 AI Agent에게 맡기되 권한은 작업 단위로 좁히고, 완료 여부는 테스트와 코드로 판정하는 시스템을 만듭니다. 아래 근거는 모두 공개된 코드와 기록에서 직접 확인할 수 있습니다.

## 대표 프로젝트

<a href="https://www.voruvi.com"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/voruvi-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/voruvi-light.svg">
  <img src="assets/voruvi-light.svg" width="100%" alt="Voruvi, 개발 중, 구 AI Supervisor. Codex와 Claude Code를 한 팀으로 실행하고, 끝나면 결과를 직접 검사합니다. 근거: Agent를 일에 넣기 전 실제로 돌려 보는 5단계 검증.">
</picture></a>

<details>
<summary><b>코드로 확인하기</b></summary>
<br>

AI Supervisor 공개 배포본의 소스는 [v0.1.0b1 릴리스](https://github.com/hyeongdongE/ai-supervisor/releases/tag/v0.1.0b1)의 wheel에서 볼 수 있습니다.

- 사전 검증: `registry/verify.py`가 격리된 임시 Git 저장소에서 Agent를 돌려 형식, 실행, 권한, 역량, 자기 역할 수행을 확인합니다.
- 최소 권한: `supervisor/permission.py`의 `decide()`는 Agent가 요청한 권한과 작업에 필요한 권한의 교집합만 줍니다.
- 결과 판정: `supervisor/pipeline.py`의 `_check_tests()`는 "통과했다"는 보고 대신 테스트를 직접 실행하고, 지적이 나오면 앞 단계로 되감습니다.

[Voruvi 웹사이트](https://www.voruvi.com) · [사례 문서](docs/projects/ai-supervisor.md)

</details>

<a href="https://github.com/hyeongdongE/hyeongdongE/blob/main/docs/projects/solopilot.md"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/solopilot-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/solopilot-light.svg">
  <img src="assets/solopilot-light.svg" width="100%" alt="SoloPilot, 공개 전. 흩어진 IT 소식을 근거가 붙은 5분 이내 브리핑으로 만듭니다. 근거: 기록 데이터 평가에서 근거 없는 주장 14건 중 0건.">
</picture></a>

<details>
<summary><b>코드로 확인하기</b></summary>
<br>

- [품질 평가 기록](https://github.com/hyeongdongE/mzapp/blob/ebacc3f89784251e31f6c27876b6dd708da4fd5b/docs/it-intelligence/quality-evaluation.md): Golden Dataset 50건에서 잘못된 병합 0/25건, 중복 누락 0/12건을 기록했습니다.
- [Golden Dataset 테스트](https://github.com/hyeongdongE/mzapp/blob/ebacc3f89784251e31f6c27876b6dd708da4fd5b/tests/intelligence/test_golden_dataset.py): 서로 다른 사건이 합쳐지는 오류를 회귀 테스트로 막습니다.
- [읽기 시간 계산](https://github.com/hyeongdongE/mzapp/blob/ebacc3f89784251e31f6c27876b6dd708da4fd5b/app/intelligence/reading_time.py): 5분 상한을 판정할 때 쓰는 기준입니다.

실제 LLM 호출은 꺼져 있고 사용자 공개 전 단계입니다. [사례 문서](docs/projects/solopilot.md)

</details>

<a href="https://github.com/hyeongdongE/hyeongdongE/blob/main/docs/projects/ai-mvp-orchestrator.md"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/orchestrator-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/orchestrator-light.svg">
  <img src="assets/orchestrator-light.svg" width="100%" alt="AI MVP Orchestrator, 프론트 승인까지 구현. 기획부터 화면 구현, 스크린샷 승인 요청까지 자동으로 잇습니다. 근거: 자동화가 끝나는 지점을 코드로 명시한 사람 승인 경계.">
</picture></a>

<details>
<summary><b>코드로 확인하기</b></summary>
<br>

- [프론트 실행 흐름](https://github.com/hyeongdongE/ai-mvp-orchestrator/blob/003c3470c28874de2a1dd13d694001e643fc29e4/src/main/java/com/aiworker/ai_mvp_orchestrator/job/service/OrchestrationRunner.java#L101-L140): 구현, 스크린샷, 승인 생성, Discord 알림을 순서대로 실행합니다.
- [승인 처리](https://github.com/hyeongdongE/ai-mvp-orchestrator/blob/003c3470c28874de2a1dd13d694001e643fc29e4/src/main/java/com/aiworker/ai_mvp_orchestrator/approval/service/ApprovalService.java): 토큰 기반으로 승인과 반려를 기록합니다.
- [AI App Template](https://github.com/hyeongdongE/ai-app-template): 파이프라인이 쓰는 실행 스크립트와 mock/API 경계입니다.

[사례 문서](docs/projects/ai-mvp-orchestrator.md)

</details>

<a href="https://github.com/hyeongdongE/hyeongdongE/blob/main/docs/projects/peakrew.md"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/peakrew-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/peakrew-light.svg">
  <img src="assets/peakrew-light.svg" width="100%" alt="Peakrew, 공공 데이터 파이프라인. 공공 데이터 8종을 공통 모델로 정리하고, 발행 여부와 이유를 규칙으로 남깁니다. 근거: 수집기 테스트 25개 통과, 2026년 11월 직접 실행.">
</picture></a>

<details>
<summary><b>코드로 확인하기</b></summary>
<br>

- [발행 판정 규칙](https://github.com/hyeongdongE/peakrew/blob/35be5688bc5af68b8c5b1eb035184653542bdff7/crawler/opportunity_crawler/publish_gate.py#L190-L237): 항목마다 통과 여부와 보류 이유를 함께 남깁니다.
- [내용 해시](https://github.com/hyeongdongE/peakrew/blob/35be5688bc5af68b8c5b1eb035184653542bdff7/crawler/opportunity_crawler/models.py#L51-L92)와 [증분 상태](https://github.com/hyeongdongE/peakrew/blob/35be5688bc5af68b8c5b1eb035184653542bdff7/crawler/opportunity_crawler/state.py): 신규, 변경, 동일 항목을 구분합니다.
- [수집기 테스트](https://github.com/hyeongdongE/peakrew/blob/35be5688bc5af68b8c5b1eb035184653542bdff7/crawler/tests/test_core.py)와 [백업 복구 리허설](https://github.com/hyeongdongE/peakrew/blob/35be5688bc5af68b8c5b1eb035184653542bdff7/.github/workflows/production-db-backup-restore-rehearsal.yml): 코드와 운영 절차를 함께 검증합니다.

[사례 문서](docs/projects/peakrew.md)

</details>

## 사용 기술

- **AI 자동화**: Claude Code, Codex, Python, Playwright
- **백엔드**: Java, Spring Boot, FastAPI, SQLAlchemy
- **데이터**: MySQL, PostgreSQL, Redis, SQLite, Flyway, Alembic
- **프론트**: TypeScript, React, React Native, Expo
- **운영**: Docker Compose, GitHub Actions, Nginx, Caddy, Cloudflare Tunnel

수치의 기준과 한계는 [검증 기록](docs/EVIDENCE.md)에 정리했습니다.
