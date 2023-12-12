from random import randint
import asyncio
from time import sleep

def odds(start, stop):
    for i in range(start, stop + 1, 2):
        yield i

def randnum():
    sleep(0.1)
    return randint(1, 40)

async def main():
    odd_values = [odd for odd in odds(2, 6)]
    odds2 = tuple(odds(2, 8))
    print(odds2)
    print(odd_values)

if __name__ == '__main__':
    main()
