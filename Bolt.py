for t in range(int(input())):
    k1,k2,k3,v = map(float,input().split())
    temp = k1*k2*k3*v
    result = round(100/temp,2)
    if result < 9.58:
        print("YES")
    else:
        print("NO")