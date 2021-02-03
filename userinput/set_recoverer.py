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
        if value is None:
            return None
        candidate = closest(value, valid_set)
        label = "Given value '{value}' is not valid, did you mean '{candidate}'?".format(
            value=value,
            candidate=candidate
        )
        if userinput(
            "set_recoverer_{candidate}".format(candidate=candidate),
            label=label,
            validator="human_bool",
            sanitizer="human_bool",
            cache=False
        ):
            return candidate
        return None
    return wrapper
