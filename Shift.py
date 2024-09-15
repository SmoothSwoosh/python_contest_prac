import asyncio


event = asyncio.Event()


async def writer(queue, delay):
    num = 0

    while not event.is_set():
        await asyncio.sleep(delay)
        await queue.put(f'{num}_{delay}')
        num += 1
        

async def stacker(queue, stack):
    while not event.is_set():
        value = await queue.get()
        await stack.put(value)


async def reader(stack, size, delay):
    for i in range(size):
        await asyncio.sleep(delay)
        value = await stack.get()
        print(value)

    event.set()


async def main():
    delay1, delay2, delay3, size = eval(input())
    
    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()
    
    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        stacker(queue, stack),
        reader(stack, size, delay3))


asyncio.run(main())
