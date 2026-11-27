#Write an asynchronous function that prints numbers from 5 to 1 with a delay of 1 second between each number. After completing the countdown, print "Time's Up!".
import asyncio
async def countdown():
    for i in range(5,0,-1):
        await asyncio.sleep(1)
        print(i)
    print("time up!")
asyncio.run(countdown())