n=int(input("Arcade Dwellers:"))

for i in range(n):
    for j in range(i+n):
        if((i+j)<=n):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")

