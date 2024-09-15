import asyncio
import copy


class FilterQueue(asyncio.Queue):
    def __contains__(self, condition):
        sample = copy.deepcopy(self)
        print(sample)
        while not sample.empty():
            #await sample.get()
            #print(num)
            if condition(num):
                return True

        return False


async def main():
    queue = FilterQueue(10)
    await queue.put(5)
    filt = lambda n: n%2
    print(filt in queue)
    #asyncio.create_task(putter(20, queue))
    #async for res in getter(20, queue, lambda n: n % 2):
    #    print(res)

asyncio.run(main())
