#4)
a=int(input("Angle Of A:"))
b=int(input("Angle Of B:"))

c=180-(a+b)
if(a==b==c):
    print("It Is An Eqilateral Triangle")
elif(a==b or a==c or b==c):
    print("It Is An Isoceles Triangle")
else:
    print('It Is Scalene Triangle')
