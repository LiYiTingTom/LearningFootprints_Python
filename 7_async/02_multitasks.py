r"""The multitasking."""
import asyncio

from utils import *


async def do_something(num):
    print(num, '-1')
    await asyncio.sleep(2)
    print(num, '-2')


async def raise_error():
    raise ValueError


@gt
async def main():
    tasks = [do_something(i) for i in range(5)]
    rerror = [raise_error() for i in range(5)]

    results = await asyncio.gather(*tasks, *rerror, return_exceptions=True)
    print(results)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

