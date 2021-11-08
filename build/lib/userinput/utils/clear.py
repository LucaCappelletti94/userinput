import os
from IPython.display import clear_output

def clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')
    clear_output(wait=True)