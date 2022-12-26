r,p = tuple(map(int , input().split()))
lis = []
lisStage = []
for _ in range(r):
    lis.append(input())
for j in range(len(lis)):
    if "***" in lis[j]:
        lisStage.append(1)
        lis[j] = lis[j][0:-4]
    else:
        lisStage.append(0)

n = int(input())

for __ in range(n):
    lisStops = input().split(' - ')
    ini = lis.index(lisStops[0])
    fin = lis.index(lisStops[1])
    c = 0
    for i in range(ini,fin+1):
        c += lisStage[i]
    if ini == 0 and fin != r-1:
        print(p*(c+1))
    elif ini != 0 and fin == r-1:
        print(p*(c+2))
    elif ini == 0 and fin == r-1:
        print(p*(c))
    else:
        print(p*(c+2))
