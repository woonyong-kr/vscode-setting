# vscode-setting

현재 VS Code 설정을 Git으로 관리하기 위한 저장소입니다.

## 구조
- `vscode-user/settings.json`: 전역 VS Code 설정
- `vscode-user/tasks.json`: 전역 태스크
- `vscode-user/snippets/*`: 전역 사용자 스니펫
- `vscode-user/profiles/woonyong/settings.json`: `woonyong` 프로필 설정
- `vscode-user/profiles/woonyong/tasks.json`: `woonyong` 프로필 태스크
- `vscode-user/profiles/woonyong/snippets/*`: `woonyong` 프로필 스니펫
- `vscode-user/extensions-global.txt`: 전역 확장 목록
- `vscode-user/profiles/woonyong/extensions.txt`: `woonyong` 프로필 확장 목록
- `scripts/export_from_vscode.py`: 현재 라이브 VS Code 설정을 이 저장소로 다시 가져오기
- `scripts/apply_to_vscode.py`: 이 저장소의 설정을 실제 VS Code에 적용하기
- `scripts/install_extensions.py`: 저장된 확장 목록을 다시 설치하기

## 사용법
현재 VS Code 상태를 저장소로 다시 가져오기:

```bash
python3 scripts/export_from_vscode.py
```

저장소 내용을 실제 VS Code에 적용하기:

```bash
python3 scripts/apply_to_vscode.py
```

확장까지 다시 설치하기:

```bash
python3 scripts/install_extensions.py
```

Git에 반영하는 기본 흐름:

```bash
python3 scripts/export_from_vscode.py
git status
git add .
git commit -m "Update VS Code settings"
git push
```

다른 기기에서 저장소 내용을 실제 VS Code에 반영하는 흐름:

```bash
git pull
python3 scripts/apply_to_vscode.py
python3 scripts/install_extensions.py
```

## 스니펫
현재 스니펫 파일은 `vscode-user/snippets`와 `vscode-user/profiles/woonyong/snippets` 아래에 들어 있습니다.

- 언어별 대표 파일 예: `python.json`, `javascript.json`
- 추가 분리 파일 예: `python-extra.code-snippets`

즉, 언어별 파일 하나만 가능한 것이 아니라:
- 언어별 대표 파일 하나를 둘 수 있고
- 같은 언어에 대해 `.code-snippets` 파일을 여러 개 더 둘 수 있습니다

`python-extra.code-snippets`는 바로 적용 가능한 예시 파일입니다.

참고:
- 언어별 전용 파일 예: `python.json`
- 추가 글로벌 파일 예: `python-extra.code-snippets`
- `.code-snippets` 파일은 `scope`를 사용해 특정 언어에만 보이게 만들 수 있습니다
