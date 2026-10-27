from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

MODEL = "gpt-6.1-terra"     # 대시보드에서 확인한 모델 이름

client = OpenAI()

response = client.responses.create(
    model=MODEL,
    input="목공이 하는 일을 2줄로 설명해줘.",
)
print(response.output_text)
print("보낸 물량 :", response.usage.input_tokens)
print("받은 물량 :", response.usage.output_tokens)

IN_PRICE = 1.00 #입력 100만 토큰당 달러
OUT_PRICE = 5.00 #출력 100만 토큰당 달러

cost = (response.usage.input_tokens * IN_PRICE + response.usage.output_tokens * OUT_PRICE)/1_000_000
print(f"이번 호출 비용: ${cost:.6f}")

