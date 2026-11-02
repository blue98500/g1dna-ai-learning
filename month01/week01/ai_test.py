from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

MODEL = "gpt-6.1-terra"     # 대시보드에서 확인한 모델 이름

client = OpenAI()

QUESTION = """아래 현장 목록을 보고 3줄로 답해.
1줄 : 예산 합계
2줄 : 면적에 비해 예산이 이상한 현장
3줄 주의 할 점 1개

- 해운대 카페, 120m², 예산 80,000,000원
- 기장 카페, 85m², 예산 55,000,000원
- 광안리 사무실, 60m², 예산 30,000,000원
- 서면 꽃집, 25m², 예산 90,000,000원"""

response = client.responses.create(
    model=MODEL,
    input= QUESTION,
)
print(response.output_text)
print("보낸 물량 :", response.usage.input_tokens)
print("받은 물량 :", response.usage.output_tokens)

IN_PRICE = 1 #입력 100만 토큰당 달러
OUT_PRICE = 5 #출력 100만 토큰당 달러

cost = (response.usage.input_tokens * IN_PRICE + response.usage.output_tokens * OUT_PRICE)/1_000_000
print(f"이번 호출 비용: ${cost:.6f}")

