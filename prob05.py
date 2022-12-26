for _ in range(int(input())):
    lis = list(input())
    i = 1
    lis2 = []
    for j in range(len(set(lis))):
        K = True
        while K:
            if lis[i] == lis[i-1]:
                pass
                i += 1
            else:
                K = False
        lis2.append(i)
        i += 1
# incomplete
