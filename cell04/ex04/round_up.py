#!/usr/bin/env python3

x = float(input("Give me a number: "))
x = float(x)
y = int(x)
if x > 0:
    if x == y:
        result = y
    else:
        result = y + 1
print(result)