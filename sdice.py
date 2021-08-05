from sys import stdin
from math import ceil
for _ in range(int(stdin.readline())):
    die_stack = []
    noofdies = int(stdin.readline())
    length = ceil(noofdies / 4)
    while noofdies > 4:
        die_stack.append(4)
        noofdies -= 4
    die_stack.append(noofdies)
    result = 0
    sides = (0, 11, 15, 18, 20)
    for i in range(length):
        side = die_stack[i]
        if i < length - 1:
            side += die_stack[i + 1]
        if die_stack[i] == 2:
            side += 2
        elif die_stack[i] == 3:
            side += 4
        elif die_stack[i] == 4:
            side += 8
        side = (die_stack[i] * 6) - side
        eachside = side // die_stack[i]
        remainingside = side % die_stack[i]
        mult = die_stack[i]
        remainingeachside = eachside
        if remainingside:
            mult -= remainingside
            remainingeachside += 1
        result += (mult * sides[eachside - 1])
        if remainingside > 0:
            result += (remainingside * sides[remainingeachside - 1])
    print(result)