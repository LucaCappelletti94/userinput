"""Set validator for user input."""
from typing import Iterable, Callable


def set_validator(
    valid_set: Iterable[str],
    normalize_to_lowercase: bool = False
) -> Callable:
    """Return set validator for given iterable of strings.

    Parameters
    -----------------
    valid_set: Iterable[str],
        Iterable of lists that compose the valid set.
    normalize_to_lowercase: bool = False,
        Whether to normalize the input to lowercase before validating.

    Returns
    -----------------
    Callable for validating the set.
    """

    def wrapper(value: str) -> bool:
        if normalize_to_lowercase:
            value = value.lower()
        return value in valid_set

    return wrapper
