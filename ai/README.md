# AI Entry Points

이 디렉터리는 사람이 읽는 문서가 아니라, AI 에이전트가 빠르게 컨텍스트를 잡고 자동 적용하기 위한 진입점이다.

읽기 순서:

1. `manifest.json`
2. `../AGENTS.md`
3. `../CLAUDE.md`
4. `../docs/platform-support-matrix.md`

규칙:

- `manifest.json` 을 machine-readable source of truth로 사용한다.
- 사람이 읽는 설명이 더 필요하면 `docs/`를 본다.
- 실제 적용 파일은 manifest의 `canonical_sources` 와 `apply_scripts` 를 따른다.
