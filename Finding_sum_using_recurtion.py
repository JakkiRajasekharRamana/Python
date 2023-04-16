def fun(N, x):
    if(N==1):
        return 1
    else:
        x=x+N
        fun(N-1, x)
        return x

N=int(input('Enter Value of N:'))
x=0
print(fun(N, x))
print(x)
