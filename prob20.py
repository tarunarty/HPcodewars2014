from itertools import permutations as pm
for _ in range(int(input())):
    c = 0
    n = int(input())
    lis = list(set(list(pm("01"*n , n))))
    for elem in lis:
        if "11" in "".join(elem):
            pass
        else:
            c+=1
    print(c)
