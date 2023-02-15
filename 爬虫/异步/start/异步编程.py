import asyncio


async def others():
    print('袖里')
    response = await asyncio.sleep(2)
    print('结束', response)
    return '返回值'


async def func():
    print('执行协程函数内部代码')
    response = await others()  # 协程对象
    print('IO请求等待结束,结果为:', response)


asyncio.run(func())
