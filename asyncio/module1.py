import asyncio

async def _add(x: int,y: int) -> int:
    await asyncio.sleep(1)
    z = x+y 
    return z 

async def main():
    res1 = _add(2,3)
    res2 = _add(7,9)

    r1 = await res1 
    print(r1)
    r2 = await res2 
    print(r2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())