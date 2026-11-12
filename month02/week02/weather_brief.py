import requests
import asyncio
import httpx

URL = "https://api.open-meteo.com/v1/forecast"
DAILY = "precipitation_probability_max"

import time

SITES = {
    "해운대": (35.16,129.16),
    "서면" : (35.16, 129.06),
    "기장" : (35.24, 129.22),
}

start = time.perf_counter()

for name, (lat, lon) in SITES.items():
    params = {
        "latitude" : lat,
        "longitude" : lon,
        "daily" : DAILY,
        "timezone" : "Asia/Seoul",
        "forecast_days" : 2,
    }

    r = requests.get(URL, params=params, timeout=10)
    if r.status_code !=200:
        print(name, "반려: ", r.status_code)
        continue
    rain = r.json()["daily"][DAILY][1]
    print(f"{name} 내일 강수 확률: {rain}%")

print(f"걸린시간 : {time.perf_counter() - start:.2f}초")

async def get_rain(client, name):
    lat, lon = SITES[name]
    params = {
        "latitude" : lat,
        "longitude" : lon,
        "daily" : DAILY,
        "timezone" : "Asia/Seoul",
        "forecast_days" : 2
    }
    r = await client.get(URL, params=params, timeout=10)
  
    if r.status_code != 200:
        return name, None
    return name, r.json()["daily"][DAILY][1]

def advice(rain):
    if rain is None:
        return "? 조회 실패 - 직접 확인"
    if rain  >= 70:
        return "! 외부 작업, 도장 주의"
    if rain  >= 40:
        return "△ 우산, 보양 준비"
    return "✓ 작업 가능"

async def main():
    start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        
        results = await asyncio.gather(
            get_rain(client, "해운대"),
            get_rain(client, "서면"),
            get_rain(client, "기장"),
        )
    print("===내일 현장 날씨 브리핑 ===")
    for name, rain in results:
        if rain is None:
            print(f"{name}: ? {advice(rain)}")
        else:
            print(f"{name}: {rain}% {advice(rain)}")

    print(f"동시에 : {time.perf_counter() - start:.2f}초")

asyncio.run(main())






