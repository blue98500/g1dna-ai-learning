# g1dna-ai-learning

인테리어 현장 10년 경력의 소장이 AI 엔지니어로 전환하는 15개월 학습 기록입니다.

## 진행 현황
| 주차 | 주제 | 산출물 |
|---|---|---|
| M1·W1 | Python 기초 + CLI | 프로젝트 관리 프로그램 |
| M1·W2 | 함수 정리 + 입력 검증 | project_manager v2 |
| M1·W3 | 경로 고정 · 클래스 · 내보내기 | project_manager v3 |
| M1·W4 | LLM API 첫 연결 | **AI Project Manager v4** |
| M2·W1 | REST API·JSON 심화 | rest_practice.py + call_ai 보강 |
| M2·W2 | async 기초 + API 프로젝트 | 현장 날씨 브리핑 |
| M2·W3 | 수학 압축 ① 벡터·행렬·임베딩 | 수학·ML 설명 노트 |

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
- 키 오류·인터넷 끊김·키 없음 **요청 형식 오류(W5 보강)**에도 프로그램이 멈추지 않음

### 알려진 한계
- AI 숫자 계산은 틀릴 수 있음 → 합계는 엑셀 공식으로 확인
- 현장 목록 전체를 AI에 보내므로 현장이 많아지면 비용 증가
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

## REST 실습 (M2·W1)
SDK 없이 `requests`로 직접 요청서를 보내 보는 연습 파일. `month02/week01/rest_practice.py`
- GET: GitHub 저장소 정보·최근 커밋 조회 (중첩 JSON 꺼내기)
- POST: OpenAI에 직접 요청 → 답·토큰·비용 해석
- 상태 코드(도장)를 먼저 확인하고 나서 내용을 꺼낸다
- API 키는 `month01/week01/.env`를 그대로 사용한다 (금고는 하나)

## 현장 날씨 브리핑 (M2·W2)

현장 여러 곳의 내일 강수확률을 **동시에** 받아서, 외부 작업·도장 주의 안내를 붙여 줍니다.

- 실행: `python month02/week02/weather_brief.py`
- 날씨 정보: Open-Meteo 공개 API (키 필요 없음)
- 좌표: 구 단위 대표 좌표만 사용 (실제 현장 주소·고객명은 넣지 않음)
- 비교: 차례로 묻기(requests) 약 2.3초 → 동시에 묻기(httpx + asyncio.gather) 약 0.9초

| 내일 강수확률 | 안내 |
|---|---|
| 70% 이상 | ⚠️ 외부 작업·도장 주의 |
| 40~69% | △ 우산·보양 준비 |
| 39% 이하 | ✅ 작업 가능 |
| 조회 실패 | ❓ 직접 확인 (한 곳이 실패해도 나머지는 계속 출력) |

연습 파일: `month02/week02/async_practice.py` (asyncio.sleep으로 동시 실행 연습)

## 수학 노트 (M2·W3)

- 노트: `month02/week03/math_notes.md` (그림 3장)
- 실행: `python month02/week03/vectors.py` · `python month02/week03/embed_search.py`
- `embed_search.py`는 OpenAI 임베딩 API를 쓰며, W5와 같은 `.env` 금고가 필요합니다
- 숫자와 현장 메모는 모두 연습용입니다