# Deployment & Updates

2026-11-04: 사용자가 생성한 빈 Public 저장소에 검증된 프로필 파일을 `main`으로 push했습니다.

- Profile: https://github.com/hyeongdongE
- Repository: https://github.com/hyeongdongE/hyeongdongE

최초 저장소 생성 요청은 연결된 인증의 `createRepository` 권한 제한으로 실패했지만, 사용자가 웹에서 저장소를 만든 뒤 Git push는 성공했습니다.

## Update Workflow

```bash
cd /workspace/hyeongdongE
git switch main
git pull --ff-only
git switch -c profile/update-description
# README, assets, docs 수정 후 검증
git add README.md assets docs scripts
git diff --cached --check
git commit -m "Update AX profile"
git push -u origin profile/update-description
gh pr create --base main --head profile/update-description --title "Update AX profile" --body "프로필 내용과 근거 문서를 갱신합니다."
```

다른 컴퓨터에서는 먼저 `git clone https://github.com/hyeongdongE/hyeongdongE.git`으로 받습니다. 인증 계정과 쓰기 권한을 확인한 뒤 실행합니다. 강제 push와 공개 범위 변경은 필요하지 않습니다.

## Review After Updating

- 프로필 README 표시, 이미지·내부 링크·사례 문서의 Mermaid를 확인합니다.
- GitHub Appearance의 light/dark 및 390px·1440px에서 Hero와 줄바꿈을 확인합니다.
- Customize your pins에서 ai-supervisor, mzapp, ai-mvp-orchestrator, peakrew 순서로 고정합니다.

추가 확인이 필요한 사실은 EVIDENCE.md와 프로젝트별 문서에 있습니다. 미확인 수치·상세 역할·수상 성과는 근거를 확보한 뒤 반영합니다.
