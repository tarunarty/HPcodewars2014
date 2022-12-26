for _ in range(int(input())):
    s = input()
    lis = list(map(int , s.split()[0]))
    num = int(s.split()[1])
    lis.reverse()
    K = False
    for i in range(len(lis)):
        if lis[i] == num:
            K = True
            break
    if i == 0:
        print("Units")
    elif i == 1:
        print("Tens")
    elif i == 2:
        print("Hundreds")
    elif i == 3:
        print("Thousands")
    elif i == 4:
        print("Ten Thousands")
    elif i == 5:
        print("Lakh")
    elif i == 6:
        print("Ten Lakhs")
    elif i == 7:
        print("Crore")
    elif i == 8:
        print("Ten Crore")
    else:
        print("Billion")
