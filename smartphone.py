inn = int(input())
k = list()
for i in range(inn):
    k.append(int(input()))
result = []
lemgth =len(k)
for i in range(lemgth):

    result.append(min(k)*lemgth)
    k = k[:k.index(min(k))]+k[k.index(min(k))+1:]
    lemgth-=1
print(max(result))
