s,r,p,n = tuple(map(int , input().split()))
pr = 0
su = 0
for _ in range(n):
    lis = input().split(';')
    lisPr = list(map(int , lis[0].split(',')))
    lisSu = list(map(int , lis[1].split(',')))
    pr += sum(lisPr)
    su += sum(lisSu)
    if pr>su:
        p -= (pr-su)*3
        
    elif pr<su:
        p += (su-pr)*4
    else:
        pass
    print(p)
