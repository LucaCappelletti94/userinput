from userinput import userinput
import pytest
import json
import os

def test_delete_cache(monkeypatch):
    path = ".tmp"
    key = "user_input"
    with open(path, "w") as f:
        json.dump({
            key: "yes"
        }, f)
    assert userinput(
        key,
        validator="human_bool",
        sanitizer="human_bool",
        always_use_default=True,
        delete_cache=True,
        cache_path=path
    )
    assert not os.path.exists(path)