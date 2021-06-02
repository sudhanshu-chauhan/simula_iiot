import asyncio
import time

import aiohttp
import pandas


async def process_frame(df):
    df.head()


async def get_frame_tasks(rurl: str, token: str):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(rurl) as resp:
            response_data = await resp.json()

            # stroke dataframe preparation
            df = pandas.DataFrame(response_data).transpose(
            ).reset_index().set_index('timestamp')

            # machine, sensor column creation
            df['machine'], df['sensor'] = df['index'].apply(
                lambda x: x.split(':')[0]), df['index'].apply(
                    lambda x: x.split(':')[1])

            # by machine grouping and yielding async tasks
            grouped_df = df.groupby('machine')
            for machine in list(grouped_df.groups.keys()):
                yield process_frame(grouped_df.get_group(machine))


async def process_response():
    rurl = 'https://localhost:8001/sensor/list'
    tasks = asyncio.gather(*[process async for process in get_frame_tasks(rurl)])
    tasks2 = asyncio.gather(*[process async for process in get_frame_tasks(rurl)])
    await tasks, tasks2

if __name__ == '__main__':
    while True:
        start = time.time()
        asyncio.run(process_response())
        end = time.time()
        print("execution time: ", end-start)
