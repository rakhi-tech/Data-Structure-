#Create an asynchronous function square(n) that waits for 2 seconds and returns the square of the given number.

#Call the function for a number and print the returned result.

import asyncio
async def square(n):
    await asyncio.sleep(2)
    return n*n
async def main():
   result= await square(2)
   print(result)
asyncio.run(main())
