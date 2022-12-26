def isPerfect(n):
    lis = []
    for i in range(1,n):
        if n%i==0:
            lis.append(i)
    if n == sum(lis):
        return True
    else:
        return False
for _ in range(int(input())):
    n = int(input())
    for i in range(2,n):
        if isPerfect(i):
            print(i,end=',')
