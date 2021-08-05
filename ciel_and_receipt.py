inn=int(input())
for k in range(inn):
    menu=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    money=int(input())
    count=0
    while money>0:
        for item in range(len(menu)-1,-1,-1):
            if money>=menu[item]:
                i,money=divmod(money,menu[item])
                count+=i
        print(count)