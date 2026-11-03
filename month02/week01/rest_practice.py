import requests

URL = "https://api.github.com/repos/blue98500/g1dna-ai-learning"

r = requests.get(URL, timeout=10)

print("도장:", r.status_code)
data = r.json()
print("저장소:", data["full_name"])
print("설명:", data["description"])
print("마지막 push:", data["pushed_at"])