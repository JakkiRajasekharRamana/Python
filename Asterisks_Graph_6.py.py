n=int(input("eNtEr nUmBeR:"))

for i in range(n):
    for j in range(n):
        if(i<=j):
            print("*",end="")
    print('\n')
