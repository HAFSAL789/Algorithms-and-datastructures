for i in range(int(input())):
    box = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(a[0]):
        for token in range(len(a)):
            if a[token] < 1:
                break
            else:
                count += 1
                a[token] -= 1
    print(count)
