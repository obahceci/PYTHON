import asyncio

'''
async def main():
    print("Hello, world!")

#print(main())   # <coroutine object main at 0x0000022233333333>    coroutine object oluşturur 

asyncio.run(main())

'''


'''

async def fetch_data(delay):

    print("fetching data...")
    await asyncio.sleep(delay)
    print("data fetched")

    return {"data":"some data"}


async def main():
   print("main function started")
   
   task=fetch_data(2)

   result=await task
   print(f"result: {result}")
   print("main function ended")



asyncio.run(main())

'''


async def fetch_data(delay,id):
    print(f"fetching data for id: {id}")
    await asyncio.sleep(delay)
    print(f"data fetched for id: {id}")
    return {"id":id}

async def main():
    task1=fetch_data(2,1)
    task2=fetch_data(2,2)

    result1=await task1

    print(f"result1: {result1}")

    result2=await task2

    print(f"result2: {result2}")


asyncio.run(main())



