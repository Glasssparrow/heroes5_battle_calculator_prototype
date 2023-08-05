from datetime import datetime


def test_time(func):
    def wrapper(*args, **kwargs):
        time_before = datetime.now()
        func(*args, **kwargs)
        time_after = datetime.now()
        print(time_after - time_before)
    return wrapper
