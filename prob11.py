for _ in range(int(input())):
    n = input()
    c = 0
    lis = list(n)
    while len(n)!=1:
        pr = 1
        for elem in lis:
            pr *= int(elem)
        n = str(pr)
        c+=1
        lis = list(n)
    print(n,c)
