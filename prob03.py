import math
for _ in range(int(input())):
    lis = input().split()
    lis1 = list(map(float , lis[0].split(',')))
    lis2 = list(map(float , lis[1].split(',')))
    d = (lis1[0]-lis2[0])**2 + (lis1[1]-lis2[1])**2 + (lis1[2]-lis2[2])**2
    print(round(math.sqrt(d),4))
