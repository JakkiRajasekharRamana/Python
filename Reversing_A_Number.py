Num=int(input("Enter Any 3 Digit Number:"))

r1=Num%10
Num=Num//10
r2=Num%10
r3=Num//10

Final_Num=((r1*100)+(r2*10)+r3)
print(Final_Num)
