def comp(p,n,r,t):
    v = p*(1 + r/n)**(n*t)
    return v

p,n,r,t = map(int, input("p,n,r,t: ").split())
print(comp(p,n,r,t))
        


