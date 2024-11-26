import datetime
from functions import test
from functions1 import test


def wait_for_print():
    from time import sleep
    sleep(3)
    print("Hello World")


print(datetime.datetime.now())
test()
