def fun(num):
    if(num<=0):
        return
    else:
        print(num%10,end="")
        return fun(num//10)
num=int(input('Enter:'))
fun(num)
