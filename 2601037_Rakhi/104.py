#Write an asynchronous function that accepts a student's name, waits for 2 seconds, and then prints:

#Welcome, [name]!

#Call the function for any three student names.
import asyncio
async def wel(name):
    await asyncio.sleep(2)
    print("welcome",name)
async def main():
    await wel("Rakhi")
    await wel("Rahul")
    await wel("uttara")
asyncio.run(main())