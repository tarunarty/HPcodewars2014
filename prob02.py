def ap(lis):
    d = lis[1]-lis[0]
    K = True
    for i in range(1,len(lis)):
        if lis[i] - lis[i-1] == d:
            pass
        else:
            K = False
            break
    return K

for _ in range(int(input())):
    lis = list(map(int , input().split(',')))
    if ap(lis):
        print("Yes")
    else:
        print("No")
