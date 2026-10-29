# g1dna-ai-learning

인테리어 현장 10년 경력의 소장이 AI 엔지니어로 전환하는 15개월 학습 기록입니다.

## 진행 현황
| 주차 | 주제 | 산출물 |
|---|---|---|
| M1·W1 | Python 기초 + CLI | 프로젝트 관리 프로그램 |
| M1·W2 | 함수 정리 + 입력 검증 | project_manager v2 |
| M1·W3 | 경로 고정 · 클래스 · 내보내기 | project_manager v3 |
| M1·W4 | LLM API 첫 연결 | **AI Project Manager v4** |

## 실행 방법 (v4 기준)
```
cd month01/week01
python -m pip install -r requirements.txt
python project_manager.py
```
처음 한 번은 `.env.example`을 복사해 `.env`를 만들고 OpenAI API 키를 넣는다.

## AI Project Manager (v4 · M1·W4)
인테리어 현장 목록을 관리하고, AI가 요약·질문 답변을 해 주는 프로그램.

### v4에서 추가된 것
- 메뉴를 보기 / 편집 / 내보내기 / AI로 묶음
- 진행상황은 design · construction · done만 입력 가능
- 엑셀 내보내기: 열 너비, 예산 쉼표, 합계 줄 자동
- 10. AI 현장 요약 / 11. AI에게 질문하기 (OpenAI API)
- 키 오류·인터넷 끊김·키 없음에도 프로그램이 멈추지 않음

### 알려진 한계
- AI 숫자 계산은 틀릴 수 있음 → 합계는 엑셀 공식으로 확인
- 현장 목록 전체를 AI에 보내므로 현장이 많아지면 비용 증가
- 예상하지 못한 API 오류(예: 요청 형식 오류)는 아직 처리 안 됨
- `ai_test.py`는 연습용 파일

## v3 (M1·W3)
- 어느 폴더에서 실행해도 같은 데이터 파일을 연다 (경로 고정)
- 새 현장은 Project 클래스(현장 카드 양식)로 등록
- 진행상황별 보기 (design / construction / done)
- 예산순·면적순 정렬 보기
- CSV · Excel 내보내기

## M1·W1 프로젝트 관리 프로그램
현장 프로젝트를 목록보기, 추가, 검색, 삭제 할 수 있는 CLI 프로그램.
데이터는 `projects.json`에 저장되어 프로그램을 꺼도 유지 됩니다.

### 이번 주 배운것
- 만든 함수는 반드시 =를 통해 받아야 변수에 담긴다.- 반만 맞은 return으로 결과를 돌려주는 함수만 
- 변수는 작업대위의 자재, 파일은 창고
- ()=실행버튼, 이름만쓰면 공구를 가리키기만 하고, ()를 붙여야 공구가 사용된다.
- 받을 상자 = 공구이름(재료)