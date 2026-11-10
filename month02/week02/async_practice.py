import asyncio

async def call_site(name, sec):
    print(f"{name}에 전화를 거는 중...")
    await asyncio.sleep(sec)
    print(f"{name} 답 옴 ({sec}초)")

asyncio.run(call_site("해운대",2))
