#short circuiting in programming language 

x=True and True and False and 3/0
print(x)
#In and statements if one false is seen(left 2 right operator) it will stop running and will not check the other operators and will return False 

y=False or True or False or 10/0
print(y)
#In or statements if one is true is seen(") it will stop running and will not check other operators and return True
