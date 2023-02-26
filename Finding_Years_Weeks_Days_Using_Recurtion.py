def fun(sec):
    if(sec==0 or sec<86400):
        return
    elif(sec%31536000!=sec):
        print('years=',sec//31536000)
        sec=sec%31536000
        return fun(sec)
    elif(sec%604800!=sec):
        print('weeks=',sec//604800)
        sec=sec%604800
        return fun(sec)
    elif(sec%86400!=sec):
        print('days=',sec//86400)
        sec=sec%86400
        return fun(sec)
sec=int(input('Enter:'))
#x=0
fun(sec)
