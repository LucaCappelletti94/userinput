from userinput import can_start

def my_test():
    assert not can_start(time=1)

def test_can_start():
    my_test()