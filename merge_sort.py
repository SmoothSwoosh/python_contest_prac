import asyncio
import random
import sys


tasks = []


def taskSort(start, finish, B, event):
    if abs(finish - start) < 2:
        event.set()
        return

    left_event = asyncio.Event()
    right_event = asyncio.Event()

    tasks.append(asyncio.create_task(merge(B, B, start, (start+finish)//2,\
                                           finish, left_event, right_event, \
                                           event)))

    taskSort(start, (start+finish)//2, B, left_event)
    taskSort((start+finish)//2, finish, B, right_event)


async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(
        event_in1.wait(),
        event_in2.wait())

    A = A.copy()
    i, j, k = start, middle, start
    while i < middle and j < finish:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i < middle:
        B[k] = A[i]
        i += 1
        k += 1

    while j < finish:
        B[k] = A[j]
        j += 1
        k += 1
    
    event_out.set()


async def mtasks(A):
    B = A.copy()

    taskSort(0, len(B), B, asyncio.Event())
    
    return (tasks, B)
    

exec(sys.stdin.read())
