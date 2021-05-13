#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x < y:
            if (x * 10 + y) != 89:
                print("{}{},".format(x, y), end=" ")
            else:
                print("{}{}".format(x, y))
