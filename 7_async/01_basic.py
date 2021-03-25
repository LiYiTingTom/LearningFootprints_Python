r"""The basic usage of async and await."""
import asyncio

from utils import *


# basic usage
@gt
async def hw(x):
    print('hw', x)
    await asyncio.sleep(x*0.1)


# using task.
async def do_something(num):
    print('start{}'.format(num))
    await asyncio.sleep(num)
    print('sleep{}'.format(num))


@gt
async def main():
    for i in range(3):
        task = asyncio.create_task(do_something(i))
        await task

if __name__ == '__main__':
    asyncio.run(hw(10))
