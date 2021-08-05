inn = int(input())
for i in range(inn):
    cars_num = int(input())
    listofcars = list(map(int,input().split()))
    count = 1

    curr_max=listofcars[0]
    for l in range(1,cars_num):
        if listofcars[l] <= curr_max:
            count +=1
            curr_max = listofcars[l]

    print(count)