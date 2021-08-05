for i in range(int(input())):
    n=int(input())
    count=0
    x=5
    while(n//x!=0):
        count=count+ n//x
        x*=5
    print(count)