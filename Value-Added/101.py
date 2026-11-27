import asyncio
async def greet():
    print("Hello!")
    await asyncio.sleep(2)
    print("Hello python")
asyncio.run(greet())