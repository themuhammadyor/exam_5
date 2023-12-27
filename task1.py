from pprint import pprint
import aiohttp

import httpx
import asyncio


class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file

    def __exit__(self, *args, **kwargs):
        self.file.close()


def printer(func):
    def inner(*args, **kwargs):
        print(func(*args, **kwargs))
        return func(*args, **kwargs)

    return inner


async def get_data():
    data = []
    i = 1
    while i < 10:
        with FileManager(f'descriptions/00{i}.txt', 'r') as f:
            fruits = f.readlines()
            # fruit_list = fruits.split('\n')
            dict1 = {'name': fruits[0].strip('\n'), 'price': fruits[1].strip('\n'),
                     'description': fruits[2].strip('\n')}
            data.append(dict1)
        i += 1
    with FileManager('descriptions/010.txt', 'r') as f:
        fruits = f.readlines()
        # fruit_list = fruits.split('\n')
        dict1 = {'name': fruits[0].strip('\n'), 'price': fruits[1].strip('\n'), 'description': fruits[2].strip('\n')}
        data.append(dict1)
    return data


async def send_request(url, client: aiohttp.ClientSession):
    response = await client.get(url)
    print("Status code", response.status_code)


async def get_comments():
    url = "https://t.me/c/1870817249/1347"
    t1 = time()
    # async with aiohttp.ClientSession() as client:
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(send_request(url.format(i), client)) for i in range(1,300)]
        await asyncio.gather(*tasks)

    t2 = time()
    print(t2 - t1)


async def run():
    # tasks = [asyncio.create_task(get_data()), asyncio.create_task(post_data)]
    # await asyncio.gather(*tasks)
    # task1 = asyncio.create_task(get_data())
    # task2 = asyncio.create_task(post_data())
    # await task1
    # await task2
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(get_data(client))]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    # url = 'https://t.me/c/1870817249/1347'
    # asyncio.run(get_data(url))
    pprint(get_data())