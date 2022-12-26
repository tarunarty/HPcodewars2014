n = int(input())
d = {10:0 , 20:0 , 30:0 , 50:0 , 100:0}
while n > 0:
    if n>99 and d[100]<3:
        n-=100
        d[100]+=1
    elif 100>n>29 and d[50]<3:
        n-=50
        d[50] += 1
    elif 30>n and d[30]<3:
        n-=30
        d[30]+=1
    elif 20>n and d[20]<3:
        n-=20
        d[20]+=1
    else:
        n-=10
        d[10]+=1
print(sum(d.values()))
if d[100] != 0:
    print(d[100] , 100)
if d[50] != 0:
    print(d[50] , 50)
if d[30] != 0:
    print(d[30] , 30)
if d[20] != 0:
    print(d[20] , 20)
if d[10] != 0:
    print(d[10] , 10)
