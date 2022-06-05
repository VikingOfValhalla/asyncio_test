import asyncio


# HOWTO:
#coroutine 
"""
async def other_function():
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

asyncio.run(other_function())
"""
# -- end HOWTO --

def define_function_numbers(func_num: int) -> str:
    func_str = "Function Number: " + str(func_num)
    return func_str

async def new_function():
    # for identifying function
    function_number = define_function_numbers(1)
    print(function_number)

    # ASYNCIO TASK CREATION
    some_text = "This is some text that I want printed"
    new_function_task = asyncio.create_task(new_function_dependent(some_text))
    # print(new_function_task)

# dependency function for new_function
async def new_function_dependent(text_to_print: str):
    function_number = define_function_numbers(2)
    print(text_to_print)

asyncio.run(new_function())
# need to create an async event loop
# an event loop handles the low level language for an async function
