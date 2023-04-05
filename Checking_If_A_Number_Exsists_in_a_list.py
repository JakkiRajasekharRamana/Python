def check(l, n):
    if(n not in l):
        return "not found"
    else:
        return l.index(n)

l = list(map(int, input().split()))
n = int(input("to find: "))

print(check(l, n))

