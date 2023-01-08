n=int(input('Enter Value n'))
i=2
ans=1
x=0
for i in range(1,n):
    while(n>0):
        ans=ans*n
        n=n-1
    x=x+(1/ans)
    i=i+1
print(ans)

