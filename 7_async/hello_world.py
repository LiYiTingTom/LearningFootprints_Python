r"""Hello world."""
import asyncio, time


async def main():
    r"""Entry point."""
    print(f"{time.ctime()} hello")
    await asyncio.sleep(1)
    print(f"{time.ctime()} world")

# 创建一个event loop的当前线程的instance。
# 如果你已经在一个async def的函数体内的话，
# 你就应该去call astbcui, get running loop()来获得当前instance.
loop = asyncio.get_event_loop()

# 我们的协程函数在放入这么一个task前是不会被执行的。
# 所以也可以理解成，我们通过create task函数来调度协程函数的任务。
# 返回的task对象可以用于监控函数的执行情况（比如是running还是dead)。
# 当然也可以用于获得你的函数执行结果。
# 另外，我们可以通过task.cancel()来终止任务
task = loop.create_task(main())

# 调用此函数会阻塞当前主线程。
# 需要注意的是run until complete()会一直运行直到给定的coro任务完成
# （如果有多个task在任务中那么要等到多个任务都完成）。
# 内部架构上看，asyncio.run()会调用run until complete，所以也会阻塞现成
loop.run_until_complete(task)

# 当主线程不阻塞后（或者被loop.stop()叫停，程序会继续向下执行。
# 这行代码的作用是找到还在pending的任务，取消，然后重新执行一遍。
pending = asyncio.all_tasks(loop=loop)

# 这通常都是最后一步。它只能对已经停止的loop执行。
# 它会清理所有的queues并且关闭executor.
# 一个停止的协程可以重启，而一个关闭的loop是无法复原的
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
