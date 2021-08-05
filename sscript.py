import re

for t in range(int(input())):
    l,k = map(int,input().split())
    s = input()
    k = re.compile("\*"*k)
    if re.search(k,s) == None:
        print("NO")
    else:
        print("YES")