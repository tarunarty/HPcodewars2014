for _ in range(int(input())):
    lis = list(map(int , input().split(',')))
    lis.sort()
    print(lis[-2],lis[1])
