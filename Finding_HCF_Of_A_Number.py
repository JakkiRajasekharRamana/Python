a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))

for i in range(a,b):
    r=b%a
    if(r==0):
        print('HCF=',a)
        break
    else:
        a=r
        
        
