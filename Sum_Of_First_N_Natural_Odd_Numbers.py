n=int(input('Enter Last Value:'))
a=int(input('Enter Start Value:'))
sum=0
for i in range(a,n+1):
    if(i%2==1):
        sum=sum+i
print(sum)
