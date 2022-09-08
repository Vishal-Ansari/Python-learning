from typing import Mapping


def st(string):
    return f"this is the heaven {string}"


def add(a, b):
    return a + b + 5


print("and the name is", __name__)
if __name__ == '__main__':
    print(st("of vishal"))
    x=add(4,6)
    print(x)