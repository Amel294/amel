import mymod

while 1:
    print'1.initialize \n 2.show \n 3. reload \n 0.exit'
    i= input('Enter your choice')
    if i==0:
        break
    elif i==1:
        a= input('enter value of a')
        b= input('enter value of b')
        c= input('enter value of c')
        d= input('enter value of d')
        e= input('enter value of e')
        mymod.a=a
        mymod.a=b
        mymod.a=c
        mymod.a=d
        mymod.a=e
    elif i==2:
        con.mymod.a+(10*mymod.b*mymod.c)-(5*mymod.d)/mymod.e
        print 'result :: ',con
    elif i==3:
        print 'reloding'
        reload(mymod)
