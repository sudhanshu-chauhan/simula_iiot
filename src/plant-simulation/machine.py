import asyncio
from functools import reduce
import csv
import random
import os

import redis


async def _start_sensor(sensor_id: str, machine_id: str, plant_id: str):
    while True:
        with redis.Redis() as r:
            r.getset(f'{plant_id}:{machine_id}:{sensor_id}', random.random())
            r.close()


async def start_machines(plant_id: str, config_file_path: str):
    with open('config_file_path', 'r') as fh:
        csvreader = csv.DictReader(fh)
        
        await asyncio.wait(
            [asyncio.create_task(
                _start_sensor(row['sensor'], row['machine'], plant_id)
            ) for row in csvreader])

if __name__ == '__main__':
    plant_id = os.environ.get('PLANT_ID')
    config_file_path =  os.environ.get('MACHINE_SENSOR_MAPFILE')
    asyncio.run(start_machines(plant_id, config_file_path))
