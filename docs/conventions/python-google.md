# Python Conventions

이 저장소의 Python 코딩 컨벤션은 Google Python Style Guide를 기준으로 한다.

참고 자료:

- Official: [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- Korean reference: [Google Python Style Guide kor](https://github.com/Yosseulsin-JOB/Google-Python-Style-Guide-kor/blob/master/Google%20Python%20Style%20Guide%20kor.md)

## Why this guide

- 팀 내에서 읽기 쉬운 코드 기준을 맞추기 쉽다.
- 함수, 클래스, 모듈 문서화 기준이 분명하다.
- AI가 코드 생성 시 일관된 스타일을 유지하기 좋다.

## Project Defaults

### Formatting

- Formatter: `ruff format`
- 기본 줄 길이: 전역 환경에서는 강제하지 않음
- 자동 포맷: 저장 시 적용

### Linting

- Linter: `ruff check`
- 의미 없는 disable 남발을 피한다.
- 네이밍, import, unused symbol, complexity 경고를 우선적으로 본다.
- 전역 환경에서는 줄 길이 경고(`E501`)를 강제하지 않는다.

### Naming

- 파일/모듈: `snake_case`
- 함수/변수: `snake_case`
- 클래스: `PascalCase`
- 상수: `UPPER_SNAKE_CASE`
- private 성격: `_leading_underscore`

### Imports

- 표준 라이브러리, 서드파티, 로컬 import를 그룹으로 나눈다.
- 와일드카드 import는 피한다.
- import 순서는 formatter/linter가 정한 규칙에 맞춘다.

### Docstrings

- 공개 함수, 클래스, 모듈은 docstring 작성을 기본으로 한다.
- 함수 설명은 “무엇을 하는지”와 “입력/출력 의미”를 먼저 적는다.
- 복잡한 부작용, 예외, 상태 변화는 명시한다.

### Exceptions

- bare `except:` 는 피한다.
- 의도한 예외만 구체적으로 잡는다.
- 실패를 무시하는 코드는 주석 또는 로깅 근거가 있어야 한다.

### Typing

- 새 코드에는 타입 힌트를 기본으로 사용한다.
- public API, 데이터 구조, 함수 반환값 타입은 가능하면 명시한다.
- 타입을 적는 것보다 오해를 줄이는 것이 우선이다.

### Comments

- 코드가 왜 그렇게 생겼는지를 설명한다.
- 코드 그대로 다시 읽어주는 주석은 피한다.
- TODO는 책임 주체나 맥락이 없으면 남기지 않는다.

## AI Coding Rules

AI 에이전트가 Python 코드를 작성할 때:

1. 기본 스타일은 Google Python Style Guide를 따른다.
2. 포맷은 `ruff format` 결과를 기준으로 본다.
3. 네이밍과 docstring은 사람이 읽기 쉬운 쪽을 우선한다.
4. 예외 처리와 import는 간결하게 유지한다.
5. 프로젝트에 기존 스타일이 더 엄격하면 프로젝트 스타일을 우선한다.
