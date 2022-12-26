from itertools import combinations
for _ in range(int(input())):
    n,r = tuple(map(int , input().split()))
    print(len(list(combinations("a"*n,r))))
