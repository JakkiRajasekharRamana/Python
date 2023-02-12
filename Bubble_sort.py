n=int(input('Enter length:'))
L=[]
for i in range(n):
    L.append(int(input('Enter:')))
#max=L[0]
for i in range(n):
    for j in range(n-i-1):
        if(L[j]>L[j+1]):
            L[j],L[j+1]=L[j+1],L[j]
print(L)
