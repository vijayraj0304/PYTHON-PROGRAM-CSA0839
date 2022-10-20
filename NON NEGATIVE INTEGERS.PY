x=list(input("Array =").split())
y=([int(i) for i in x])
area=0
for i in range(len(y)) :
    for j in range(i + 1,len(y)) :
        area = max(area, min(y[j],y[i]) * (j - i))
print(area)
