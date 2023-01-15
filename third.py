import os
import os.path

def x():
    a = os.listdir()
    print(len(a))

    for b in a:
        if os.path.isdir(b):
            print("|" + b)
        else:
            print(b)

x()