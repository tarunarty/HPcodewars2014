from itertools import combinations as cb
for _ in range(int(input())):
    n = int(input())
    for r in range(n+1):
        print(len(list(cb("a"*n,r))) , end = " ")
