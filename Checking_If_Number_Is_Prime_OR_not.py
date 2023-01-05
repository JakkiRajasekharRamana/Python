num=int(input('Enter A Number'))
count=0
for i in range(2,num+1):
    if(num%i==0):
        count=count+1
        

print(count)
if(count==1):
    print("It is a prime number")
else:
    print('Not A Prime Number')
