n=int(input("Enter Value:"))

for i in range(n//2 + 1):
    for j in range(i+1):
        print("*",end="")
    print("\n")
    

for i in range(n//2,0,-1):
    for j in range(i):
            print("*",end="")
    print("\n")
