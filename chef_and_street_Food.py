for _ in range(int(input())):
    result = 0
    for _ in range(int(input())):
        s,p,v = map(int,input().split())
        profit = (p//(s+1))*v
        if profit > result:
            result = profit
    print(result)