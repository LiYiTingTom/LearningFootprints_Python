r"""The basic usage of async and await."""
import asyncio

from utils import *

ANS = {'ac':[], 'c':[]}

# basic usage
@gt
async def hw(x):
    print('hw', x)
    await asyncio.sleep(x*0.1)


async def acalculate(floor, ceil):
    ans = 1
    for i in range(floor, ceil * 100):
        for j in range(floor, ceil * 100):
            for k in range(floor, ceil * 100):
                ans *= k
                if ans > 100: ans = pow(ans, 0.3)
    ANS['ac'].append(ans)
    return ans


def calculate(floor, ceil):
    ans = 1
    for i in range(floor, ceil * 100):
        for j in range(floor, ceil * 100):
            for k in range(floor, ceil * 100):
                ans *= k
                if ans > 100: ans = pow(ans, 0.3)
    ANS['c'].append(ans)
    return ans


# using task.
async def do_something(num):
    print('start{}'.format(num))
    await asyncio.sleep(num)
    print('sleep{}'.format(num))


@gt
async def main():
    for i in range(3):
        task = asyncio.create_task(acalculate(1, i))
        await task

if __name__ == '__main__':
    p_time = time.time()
    asyncio.run(main())
    print(time.time() - p_time)

    p_time = time.time()
    for i in range(1, 3):
        calculate(1, i)
    print(time.time() - p_time)
    print(ANS)
