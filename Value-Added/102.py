#Write an asynchronous function to print numbers from 1 to 5. The program should wait for 1 second between printing each number.
import asyncio
async def number():
    for i in range(1,6):
        await asyncio.sleep(1)
        print(i,end=" ")
asyncio.run(number())