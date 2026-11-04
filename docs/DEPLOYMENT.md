# Deployment

로컬 구현과 커밋은 완료했습니다. 현재 연결된 GitHub 인증은 새 저장소 생성 요청을 `Resource not accessible by integration (createRepository)`로 거부했습니다. 원격 생성·push는 이루어지지 않았습니다.

## 저장소 생성 권한이 있는 인증 환경

GitHub의 사용자명과 인증 계정을 확인한 뒤 실행합니다. 아래 명령은 현재 없는 Public 프로필 저장소를 새로 생성합니다.

```bash
cd /workspace/hyeongdongE
gh auth status
gh repo create hyeongdongE/hyeongdongE --public --description 'AI Transformation · AI Agent Systems · Backend Engineering' --source . --remote origin --push
```

또는 GitHub 웹에서 README 초기화 없이 Public `hyeongdongE/hyeongdongE`를 생성한 뒤:

```bash
cd /workspace/hyeongdongE
git remote add origin https://github.com/hyeongdongE/hyeongdongE.git
git push -u origin main
```

다운로드한 ZIP은 Git 이력을 제외한 파일 스냅샷입니다. 다른 위치에서 푼 경우 해당 폴더에서 먼저 실행합니다.

```bash
git init -b main
git add README.md assets docs
git commit -m "Build evidence-based AX profile"
```

이후 위 배포 명령의 `cd` 경로를 조정합니다. 기존 원격이 설정되어 있다면 `git remote -v`로 확인하고 중복 추가하지 않습니다. 원격에 기존 커밋이 생겼다면 강제 push하지 않고 별도 브랜치·PR로 통합합니다.

## 반영 후 확인

- https://github.com/hyeongdongE 에 프로필 README가 표시되는지 확인합니다.
- GitHub Appearance의 light/dark 및 390px·1440px에서 Hero·줄바꿈·이미지를 확인합니다.
- 사례 문서의 Mermaid 다이어그램과 링크를 실제 GitHub에서 확인합니다.
- Customize your pins에서 Supervisor, Orchestrator, Peakrew, Template 순서로 고정합니다.

공개 전 추가 확인 항목은 EVIDENCE.md와 프로젝트별 문서에 있습니다. 현재 문서는 확인되지 않은 수치·상세 역할·수상 성과를 주장하지 않습니다.
