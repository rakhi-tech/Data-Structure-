import asyncio
async def greet():
    print("hello Rahul!")
    await asyncio.sleep(4)
    print("welcome Rahul!")
async def main():
    await asyncio.gather(greet(),greet())
    
asyncio.run(main())
