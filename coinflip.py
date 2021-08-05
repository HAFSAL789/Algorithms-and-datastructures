for _ in range(int(input())):
    for i in range(int(input())):
        li = list(map(int,input().split()))
        head = 0
        tail = 0
        if li[1] %2 == 0:
            print(li[1]//2)
        else:
            if li[0] == 1:

                tail = li[1]//2+1
                head = li[1] - tail
            else:

                head = li[1]//2+1
                tail = li[1] - head
            if li[2] == 1:
                print(head)
            else:
                print(tail)