c1, c2 ,c3 = map(int,input().split())
s = set([c1,c2,c3])
if len(s) < 3:
    print("YES")
else:
    print("NO")