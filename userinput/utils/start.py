from .clear import clear
import time

def can_start(message:str="Type CTRL+C to start [{i} seconds remaining]", interval:int=10)->bool:
    """Return boolean representing if user wants to start task.
        message:str="Type CTRL+C to start [{i} seconds remaining]", message to show to the user.
        interval:int=10, the interval to be waited for.
    """
    try:
        clear()
        for i in reversed(range(interval)):
            print(message.format(i=i))
            time.sleep(1)
            clear()
        return False
    except KeyboardInterrupt:
        return True    