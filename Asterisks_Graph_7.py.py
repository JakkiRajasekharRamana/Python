for i in range(5):
    for j in range(i+1):
        if(i>=j and j==0):
            print('1',end="")
        elif(i>=j and j>0):
            print('*',end="")
    print('\n')
