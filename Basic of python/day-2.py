## Multiple Async functions

import time
import asyncio

async def task1():
    await asyncio.sleep(2)
    return "task-1 done.."

async def task2():
    await asyncio.sleep(1)
    return "task-2 done.."

async def main():
    start = time.perf_counter()
    # asyncio.gather returns a future (awaitable) that resolves to a list of results
    results = await asyncio.gather(task1(), task2()) 
    end = time.perf_counter()
    
    print(f"Results: {results}")
    print(f"Execution time: {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())