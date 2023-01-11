n=int(input("Enter Value:"))
L=[]
product=1
for i in range(n):
    L.append(int(input("Enter:")))
    product=product*L[i]
print(product)
