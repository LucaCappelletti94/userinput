import os
from environments_utils import is_notebook, is_colab


def clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')
    if is_notebook() or is_colab():
        from IPython.display import clear_output
        clear_output(wait=True)