import requests

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude" : 35.16,
    "longitude" : 129.16,
    "daily" : "precipitation_probability_max",
    "timezone" : "Asia/Seoul",
    "forecast_days" : 2,
}

r = requests.get(URL, params=params, timeout=10)
print("도장:", r.status_code)
print("실제 주소:", r.url)
data = r.json()
print(data["daily"]["time"])
print("내일 강수 확률:",data["daily"]["precipitation_probability_max"][1])

