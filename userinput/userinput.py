from typing import Callable, Union, List
import json
import os
from inspect import isfunction
import getpass
from .utils import default_validators, closest, default_sanitizers, clear


def normalize_validators(validator: str) -> List[Callable]:
    if validator not in default_validators:
        candidate = closest(validator, default_validators.keys())
        if candidate is None:
            raise ValueError("Given validator callback {validator} is not available.".format(
                validator=validator))
        raise ValueError("Given validator callback {validator} is invalid, did you mean {candidate}?.".format(
            validator=validator,
            candidate=candidate
        ))
    return default_validators.get(validator)


def normalize_sanitizers(sanitizer: str) -> List[Callable]:
    if sanitizer not in default_sanitizers:
        candidate = closest(sanitizer, default_sanitizers.keys())
        if candidate is None:
            raise ValueError("Given sanitizer callback {sanitizer} is not available.".format(
                sanitizer=sanitizer))
        raise ValueError("Given sanitizer callback {sanitizer} is invalid, did you mean {candidate}?.".format(
            sanitizer=sanitizer,
            candidate=candidate
        ))
    return default_sanitizers.get(sanitizer)


def _is_input_valid(value: str, validators: List) -> bool:
    return not validators or all([v(value) for v in validators])


def multi_line_input(label: str):
    return "\n".join(iter(lambda: input(label), ''))


def userinput(
    name: str,
    label: str = "Please insert {name}",
    default=None,
    always_use_default: bool = False,
    hidden: bool = False,
    validator: Union[Callable, List[Union[Callable, str]], str] = None,
    maximum_attempts: int = 100,
    recoverer: Callable = None,
    sanitizer: Union[Callable, List[Union[Callable, str]], str] = None,
    cache: bool = True,
    cache_path: str = ".userinput.json",
    delete_cache: bool = False,
    auto_clear: bool = False,
    multi_line: bool = False
) -> str:
    """Default handler for uniform user experience.

    Parameters
    ----------------------------------------------
    name:str,
        Name of the expected input, used for storing.
    label:str="Please insert {name}",
        Label shown to the user.
    default=None,
        Default value to use.
    hidden:bool=False,
        Whetever to display or not user input.
    always_use_default:bool=False,
        Whetever to always use the default, bypassing the user request.
    validator:Union[Callable, List[Union[Callable, str]], str]=None,
        Single or list of validators for the user input.
    maximum_attempts:int=100,
        Maximum available attempts for a given input.
        By default 100 to avoid deadlocks.
    recoverer: Callable, str]=None,
        Single or list of recoverer to use when the input fails but could be
        sanitized into something acceptable.
    sanitizer:Union[Callable, List[Union[Callable, str]], str]=None,
        Single or list of sanitizers for the user input.
    cache:bool=True,
        Whetever to load and store input values.
    cache_path:str=".userinput.json",
        Default path to store and load cache.
    delete_cache:bool=False,
        Whetever to delete cache after reading it.
    auto_clear:bool=False,
        Whetever to call clear stdout after user input is determined.
    """
    defaults = {}
    if cache and os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            defaults = json.load(f)
            default = defaults.get(name, default)
    if isinstance(validator, str) or isfunction(validator):
        validators = [validator]
    else:
        validators = []
    if isinstance(sanitizer, str) or isfunction(sanitizer):
        sanitizers = [sanitizer]
    else:
        sanitizers = []
    validators = [
        normalize_validators(validator) if isinstance(validator, str) else validator for validator in validators
    ]
    sanitizers = [
        normalize_sanitizers(sanitizer) if isinstance(sanitizer, str) else sanitizer for sanitizer in sanitizers
    ]
    attempts = 0

    input_function = None
    if hidden:
        input_function = getpass.getpass
    elif multi_line:
        input_function = multi_line_input
    else:
        input_function = input

    while maximum_attempts is None or attempts < maximum_attempts:
        value = None
        if not always_use_default or not _is_input_valid(default, validators):
            value = input_function("{label}{default}: ".format(
                label=label.format(name=name),
                default="" if default is None else " [{}]".format(default)
            )).strip()
        if not value:
            value = default
        if recoverer is not None and not _is_input_valid(value, validators):
            recoverered = recoverer(value)
            if recoverered is not None:
                value = recoverered
        if _is_input_valid(value, validators):
            if cache and not delete_cache and (name not in defaults or value != defaults[name]):
                with open(cache_path, "w") as f:
                    defaults[name] = value
                    json.dump(defaults, f, indent=4)
            if delete_cache:
                os.remove(cache_path)
            if auto_clear:
                clear()
            for sanitizer in sanitizers:
                value = sanitizer(value)
            return value
        attempts += 1
        print("Given value '{value}' is not valid.".format(value=value))
    raise ValueError(
        "User attempted to answer query called {name} more than {attempts} times!".format(
            name=name,
            attempts=attempts
        )
    )
