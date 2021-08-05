test = int(input())
for i in range(test):
    list1=list(map(int,input().split()))
    list1 = list1[1:]
    x = 1
    minimum = min(list1)
    l=[]
    list2=[]
    list3=[]
    for i in list1:
        if i%minimum==0:
            list2.append(i//minimum)
        else:
            list2.clear()
            break
    if len(list2)==0:
        while x<=minimum:
            if minimum%x==0:
                list3 =[True if j%x==0 else False for j in list1]
                if False not in list3:
                    l.append(x)
            x+=1
    if len(list2)==0:
        ll=[i//max(l)for i in list1]
        print(*ll)
    else:
        print(*list2)