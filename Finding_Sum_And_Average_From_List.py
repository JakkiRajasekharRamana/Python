def funtion(L):
    x=sum(L)
    length=len(L)
    return x/length
L=[]
n=int(input('Enter no of elements in list:'))
for i in range(n):
    L.append(int(input('Enter:')))
print('Average=',funtion(L))

