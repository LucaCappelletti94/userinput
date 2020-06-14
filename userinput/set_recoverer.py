from typing import Iterable, Callable
from .utils.closest import closest
from .userinput import userinput


def set_recoverer(valid_set: Iterable[str]) -> Callable:
    """Return set recoverer for given iterable of strings.

    Parameters
    -----------------
    valid_set: Iterable[str],
        Iterable of lists that compose the valid set.

    Returns
    -----------------
    Callable for recovering a value from the set.
    """
    def wrapper(value: str) -> str:
        candidate = closest(value, valid_set)
        label = "Given value {value} is not valid, did you mean {candidate}?".format(
            value=value,
            candidate=candidate
        )
        if userinput("set_recoverer", label=label, validator="human_bool"):
            return candidate
        return None
    return wrapper