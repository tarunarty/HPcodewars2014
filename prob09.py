import math
for _ in range(int(input())):
    d = int(input())
    theta = math.atan(5.3/d)
    theta = math.degrees(theta)
    print(round(theta,2))
