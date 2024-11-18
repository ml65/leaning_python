# Домашнее задание по теме "Асинхронность на практике"
import time
import asyncio

# Задача "Асинхронные силачи":

async def start_strongman(name, power):
    if (validate(name,power)):
        print(f"Силач {name} начал соревнования.")
        for ball in range(1,6):
            print(f"Силач {name} поднял шар {ball}")
            await asyncio.sleep(1/power)
        print(f"Силач {name} закончил соревнования.")
    else:
        print(f"Параметры не прошли валидацию {name} {power}. Спортсмен отстранен от соревнований!")

def validate(name, power):
    res = True
    if not isinstance(name, str):
        res = False
    if not isinstance(power, int):
        res = False
    return res

async def start_tournament():
    power = {
        'Pasha':3,
        'Denis':4,
        'Apollon':5
    }
    tasks = list()
    for name in power:
        tasks.append(asyncio.create_task(start_strongman(name, power[name])))

    for task in tasks:
        await task

start = time.time()
asyncio.run(start_tournament())
finish = time.time()
