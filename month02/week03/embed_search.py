import math
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR.parent.parent / "month01" /"week01"/ ".env"
load_dotenv(ENV_PATH)

EMBED_MODEL = "text-embedding-3-small"

MEMOS = [
    "카페 바닥 에폭시 시공",
    "카페 바닥 타일 교체",
    "사무실 천장 조명 교체",
    "옥상 우레탄 방수 공사",
    "화장실 바닥 방수 보수",
]

def dot(a,b):
    total = 0
    for i in range(len(a)):
        total = total +a[i] * b[i]
    return total

def norm(a):
    return math.sqrt(dot(a,a))

def cosine(a,b):
    return dot(a,b) / (norm(a)*norm(b))

client = OpenAI()
r = client.embeddings.create(model=EMBED_MODEL, input=MEMOS)

vectors = []
for d in r.data:
    vectors.append(d.embedding)

print("메모 수:", len(vectors))
print("칸 수:", len(vectors[0]))

for i in range(len(MEMOS)):
    for j in range(i+1, len(MEMOS)):
        print(f"{cosine(vectors[i],vectors[j]):.3f} {MEMOS[i]} ⇿ {MEMOS[j]}")


