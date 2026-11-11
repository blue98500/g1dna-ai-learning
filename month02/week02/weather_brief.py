import requests
import asyncio
import httpx

URL = "https://api.open-meteo.com/v1/forecast"

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
        "daily" : "precipitation_probability_max",
        "timezone" : "Asia/Seoul",
        "forecast_days" : 2,
    }

    r = requests.get(URL, params=params, timeout=10)
    if r.status_code !=200:
        print(name, "반려: ", r.status_code)
        continue
    rain = r.json()["daily"]["precipitation_probability_max"][1]
    print(f"{name} 내일 강수 확률: {rain}%")

print(f"걸린시간 : {time.perf_counter() - start:.2f}초")

async def get_rain(client, name):
    lat, lon = SITES[name]
    params = {
        "latitude" : lat,
        "longitude" : lon,
        "daily" : "precipitation_probability_max",
        "timezone" : "Asia/Seoul",
        "forecast_days" : 2
    }
    r = await client.get(URL, params=params, timeout=10)
  
    if r.status_code != 200:
        return name, None
    return name, r.json()["daily"]["precipitation_probability_max"][1]

async def main():
    start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        
        results = await asyncio.gather(
            get_rain(client, "해운대"),
            get_rain(client, "서면"),
            get_rain(client, "기장"),
        )
    for name, rain in results:
        print(f"{name} 내일 강수확률 : {rain}%")
    print(f"동시에 : {time.perf_counter() - start:.2f}초")

asyncio.run(main())






