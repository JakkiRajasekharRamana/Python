num=int(input('Enter Any Number:'))
r=0
x=num
while(num>0):
    r=r*10+num%10
    num=num//10
print(r)
if(x==r):
    print('Given Number Is Palindrome')
else:
    print('Not A Palindrome Number')
