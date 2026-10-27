from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

MODEL = "gpt-6.1-terra"     # 대시보드에서 확인한 모델 이름

client = OpenAI()

response = client.responses.create(
    model=MODEL,
    input="인테리어 현장에서 '목공'이 하는 일을 한 문장으로 설명해줘.",
)
print(response.output_text)