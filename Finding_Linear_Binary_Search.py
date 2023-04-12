def linear(l, n):
    for i in range(len(l)):
        if(l[i] == n):
            return i
    return "not found"

def binary(l,n):
    s = 0
    e = len(l)-1
    while(s <= e):
        m = (s+e)//2
        if(l[m] == n):
            return m
        elif(l[m] < n):
            s = m+1
        elif(l[m] > n):
            e = m-1
    return "not found"

l = list(map(int, input("list: ").split()))
n = int(input("to find: "))

print(linear(l,n))
l.sort()
print("sorted list for binary search...", l)
print(binary(l,n))
