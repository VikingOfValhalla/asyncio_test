import asyncio

#coroutine 
async def main():
    # will return a coroutine object
    print('tom')
    task = asyncio.create_task(foo('text'))
    await task
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)
# need to await for it's execution
# await must be inside async function
asyncio.run(main())



# need to create an async event loop
# an event loop handles the low level language for an async function
