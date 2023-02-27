def fun(num):
    if(num==0):
        return
    else:
        fun(num//10)
        print(num%10)
num=int(input('Enter:'))
fun(num)
