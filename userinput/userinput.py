from typing import Callable, Union, List
import json
import os
from inspect import isfunction
from getpass import getpass
from .utils import default_validators, closest, default_sanitizers, clear

def normalize_validators(validator:str)->List[Callable]:
    if validator not in default_validators:
        candidate = closest(validator, default_validators.keys())
        if candidate is None:
            raise ValueError("Given validator callback {validator} is not available.".format(validator=validator))
        raise ValueError("Given validator callback {validator} is invalid, did you mean {candidate}?.".format(
            validator=validator,
            candidate=candidate
        ))
    return default_validators.get(validator)

def userinput(
    name:str, 
    label:str="Please insert {name}",
    default=None,
    always_use_default:bool=False,
    hidden:bool=False,
    validator:Union[Callable, List[Callable], List[Union[Callable, str]], str, List[str]]=None,
    maximum_attempts:int=None,
    sanitizer:Union[Callable, str]=None,
    cache:bool=True,
    cache_path:str=".userinput.json",
    delete_cache:bool=False,
    auto_clear:bool=False
    )->str:
    """Default handler for uniform user experience.
        name:str, name of the expected input, used for storing.
        label:str="Please insert {name}", label shown to the user.
        default=None, default value to use.
        hidden:bool=False, whetever to display or not user input.
        always_use_default:bool=False, whetever to always use the default, bypassing the user request.
        validator:Union[Callable, List[Callable], List[Union[Callable, str]], str, List[str]]=None, single or list of validators for the user input.
        maximum_attempts:int=None, maximum available attempts for a given input.
        sanitizer:Union[Callable, List[Callable], str]=None, function or string used to sanitize input.
        cache:bool=True, whetever to load and store input values.
        cache_path:str=".userinput.json", default path to store and load cache.
        delete_cache:bool=False, whetever to delete cache after reading it.
        auto_clear:bool=False, whetever to call clear stdout after user input is determined.
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
    if isinstance(sanitizer, str):
        sanitizer = default_sanitizers.get(sanitizer, None)
    validators = [
        normalize_validators(validator) if isinstance(validator, str) else validator for validator in validators
    ]
    attempts = 0
    input_function = getpass if hidden else input 
    while maximum_attempts is None or attempts<maximum_attempts:
        value = None
        if not always_use_default:
            value = input_function("{label}{default}: ".format(
                label=label.format(name=name),
                default="" if default is None else " [{default}]".format(default=default)
            )).strip()
        if not value:
            value = default
        if not validators or all([v(value) for v in validators]):
            if cache and not delete_cache:
                with open(cache_path, "w") as f:
                    defaults[name] = value
                    json.dump(defaults, f, indent=4)
            if delete_cache:
                os.remove(cache_path)
            if auto_clear:
                clear()
            return value if sanitizer is None else sanitizer(value)
        attempts+=1
        print("Given value {value} is not valid.".format(value=value))