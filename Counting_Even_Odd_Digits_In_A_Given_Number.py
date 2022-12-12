#8)
num=int(input('Enter Any 4 digit Number:'))

count_odd=0
count_even=0

if(num%2==0):
    count_even=count_even+1
else:
    count_odd=count_odd+1

num=num//10
if(num%2==0):
    count_even=count_even+1
else:
    count_odd=count_odd+1

num=num//10
if(num%2==0):
    count_even=count_even+1
else:
    count_odd=count_odd+1

num=num//10
if(num%2==0):
    count_even=count_even+1
else:
    count_odd=count_odd+1

print("Even Digits=",count_even)
print("Odd Digits=",count_odd)
