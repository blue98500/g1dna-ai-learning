import asyncio
import time


async def call_site(name, sec):
    print(f"{name}에 전화를 거는 중...")
    await asyncio.sleep(sec)
    print(f"{name} 답 옴 ({sec}초)")

async def main():
    start = time.perf_counter()
    await asyncio.gather(
        call_site("해운대", 2),
        call_site("서면", 1),
        call_site("기장", 3),
    )
    print(f"동시에: {time.perf_counter() - start:.2f}초")

asyncio.run(main())

