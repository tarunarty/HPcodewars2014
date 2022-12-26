for _ in range(int(input())):
    k = str(int(input())+1)
    K = True
    while K:
        if k[::-1] == k:
            break
        else:
            k = str(int(k)+1)
    print(k)
