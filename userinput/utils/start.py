from .clear import clear
from typing import Callable
from time import sleep

def can_start(message:str="Type CTRL+C to start [{i} seconds remaining]", time:int=10)->bool:
    """Return boolean representing if user wants to start task.
        message:str="Type CTRL+C to start [{i} seconds remaining]", message to show to the user.
        time:int=10, the time to be waited for.
    """
    try:
        clear()
        for i in reversed(range(time)):
            print(message.format(i=i))
            sleep(1)
            clear()
        return False
    except KeyboardInterrupt:
        return True    