import asyncio

# asyncio async await
#  План:
# 1. Asyncio фреймворк для создания событийных циклов
# 2. Пример простой асинхронной программы времён Python 3.4
# 3. Синтаксис async/await  на замену @asyncio.coroutine и yield from
# 4. Пример асинхронного скачивания файлов


# Event Loop:
#    coroutine > Task (Future)

# @asyncio.coroutine
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        # yield from asyncio.sleep(0.1) 
        await asyncio.sleep(0.1)

# @asyncio.coroutine
async def print_time():
    count = 0 
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        # yield from asyncio.sleep(0.1)
        await asyncio.sleep(0.1)

# @asyncio.coroutine
async def main():
    # Очередь событийного цикла
    # task1 = asyncio.ensure_future(print_nums()) # создание объекта будущего
    # task2 = asyncio.ensure_future(print_time())
    
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    # yield from asyncio.gather(task1, task2)
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())