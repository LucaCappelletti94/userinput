from typing import Iterable, Callable


def set_validator(valid_set: Iterable[str]) -> Callable:
    """Return set validator for given iterable of strings.

    Parameters
    -----------------
    valid_set: Iterable[str],
        Iterable of lists that compose the valid set.

    Returns
    -----------------
    Callable for validating the set.
    """
    def wrapper(value: str) -> bool:
        return value in valid_set
    return wrapper
