n=int(input('Enter length:'))
l=[]
for i in range(n):
    l.append(int(input('Enter:')))

#bubble
'''
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(L)
'''
#insertion
for i in range(1, len(l)):
    key = l[i]
    j = i-1
    while(j >= 0 and key<l[j]):
        l[j+1] = l[j]
        j -= 1
    l[j+1] = key
print(l)
'''
#selection
for i in range(len(l)):
    m = i
    for j in range(i+1, len(l)):
        if(l[j] < l[m]):
            m = j
    l[m], l[i] = l[i], l[m]
print(l)
'''
