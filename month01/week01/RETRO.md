# M1·W1 회고 — Python Core (2026-10-14)

## 만든 것
- `project_manager.py`: 인테리어 현장 목록을 목록·추가·검색·삭제하는 CLI 프로그램
- 데이터는 `projects.json`에 저장 (0번 종료 시 자동 저장)

## 비유 정리
| 코드 | 현장 비유 |
|---|---|
| 변수 (`projects`) | 작업대 위 자재 |
| 파일 (`projects.json`) | 창고 |
| 함수 (`save_projects()`) | 공구 |
| `()` | 공구 전원 버튼 |
| Git / GitHub | 공사 사진대장 / 전시실 |

공식: `받을그릇 = 공구이름(재료)` — return하는 함수만 `=`로 받는다.

## 하자 기록
| 내가 쓴 코드 | 정답 |
|---|---|
| `projects() = load_projects` | `projects = load_projects()` |
| `show_projects = (projects)` | `show_projects(projects)` |
| `save_projects` | `save_projects(projects)` |
| `add_project()` | `add_project(projects, name, area, budget)` |

## 다음 주(W2)에 고칠 것
- 면적·예산에 글자 입력 시 `ValueError`로 멈춤 → Exception (`try`/`except`)
- 진행 상황 수정 기능 없음 → Class로 구조 정리 후 추가

## 느낀 점
꾸준히 하면 잊지 않을 것도 쉬고 나니 처음부터 다시 떠올려야 했다. 매일 조금씩 하는 시스템을 만들었으니 현장 상황에 맞춰 멈추지 않고 가겠다.