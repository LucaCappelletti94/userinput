from userinput import can_start
import time


def interrupt(seconds):
    raise KeyboardInterrupt("Test")


def test_can_start():
    assert not can_start(interval=1)


def test_not_can_start(monkeypatch):
    monkeypatch.setattr(time, 'sleep', interrupt)
    assert can_start(interval=5)
