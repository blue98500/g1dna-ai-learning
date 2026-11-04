import requests

URL = "https://api.github.com/repos/blue98500/g1dna-ai-learning"

r = requests.get(URL, timeout=10)

print("도장:", r.status_code)
data = r.json()
print("저장소:", data["full_name"])
print("설명:", data["description"])
print("마지막 push:", data["pushed_at"])

URL2 = "https://api.github.com/repos/blue98500/g1dna-ai-learning/commits"

r = requests.get(URL2, timeout=10)
if r.status_code != 200:
    print("반려:", r.status_code)
else:
    commits = r.json()                # 리스트 (커밋이 줄 서 있음)
    first = commits[0]              # 가장 최근 커밋 하나 (사전)
    print(first["commit"]["message"])
    print(first["commit"]["author"]["date"])

for c in commits[:5]:
    print(c["commit"]["message"])
    print(c["commit"]["author"]["date"])
