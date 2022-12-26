import numpy as np
lis = np.array([0,0,0,0])
for i in range(int(input())):
    lis1 = list(map(int , input().split()))
    t = lis1.pop()
    lis += np.array(lis1)
    if lis[i%4] - 36*t <0:
        lis[i%4] = 0
    else:
        lis[i%4] -= 36*t
    print(lis)
