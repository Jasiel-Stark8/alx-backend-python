from time import sleep, time
import asyncio

async def brewCoffee():
    print('Brewing Coffee')
    await asyncio.sleep(3)
    print('Coffee done')
    return 'Coffee ready'
    
async def toast():
    print('Toasting bread')
    await asyncio.sleep(1)
    print('Done toasting')
    return 'Toast ready'

async def main():
    start = time()

    # way 1
    # batch = asyncio.gather(brewCoffee(), toast())
    # coffee_result, toast_result = await batch

    # Way 2
    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toast())

    result_coffee = await coffee_task
    result_toast = await toast_task

    end = time()
    total_time = end - start

    print(f'coffee result: {result_coffee}')
    print(f'toast results: {result_toast}')
    print(f'total time: {total_time:.2f}')

if __name__ == '__main__':
    asyncio.run(main())
