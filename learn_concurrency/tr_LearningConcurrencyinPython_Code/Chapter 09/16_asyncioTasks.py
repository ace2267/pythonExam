import asyncio

async def myCoroutine():
  print("My Coroutine")

async def main():
  await asyncio.sleep(1)
#  current=asyncio.Task.current_task()
#  print(current)

loop = asyncio.get_event_loop()
try:
  task1 = loop.create_task(myCoroutine())
  task2 = loop.create_task(myCoroutine())
  task3 = loop.create_task(myCoroutine())
#  task3.cancel()
  pending = asyncio.Task.all_tasks()
  print(pending)
  loop.run_until_complete(main())
finally:
  loop.close()
