import math
inn = int(input())
for i in range(inn):
    k=input()
    length = len(k)
    d={}
    d1 = {}
    k1 = k[:length // 2]
    for i in k[:length // 2]:
        d[i] = k1.count(i)

    if length % 2 == 0:
        k2 = k[len(k)//2:]

        for i in k2:
            d1[i] = k2.count(i)
    else:
        k2 = k[math.ceil(length/2):]
        for i in k2:
            d1[i] = k2.count(i)
    if d == d1:
        print("YES")
    else:
        print("NO")