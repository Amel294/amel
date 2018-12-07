from Tkinter import *
mwin=Tk()
vexp=''
def bhan(ch):
 global vexp
 if ch=='=':
  vexp=str(eval(vexp))
 else:
  vexp+=ch
 t1.set(str(vexp))
mwin.title('calc')
t1=StringVar()
e1=Entry(mwin,textvariable=t1)
b1=Button(mwin,text='1',command=lambda:bhan('1'))
b2=Button(mwin,text='2',command=lambda:bhan('2'))
b3=Button(mwin,text='3',command=lambda:bhan('3'))
b4=Button(mwin,text='4',command=lambda:bhan('4'))
b5=Button(mwin,text='5',command=lambda:bhan('5'))
b6=Button(mwin,text='6',command=lambda:bhan('6'))
b7=Button(mwin,text='7',command=lambda:bhan('7'))
b8=Button(mwin,text='8',command=lambda:bhan('8'))
b9=Button(mwin,text='9',command=lambda:bhan('9'))
b0=Button(mwin,text='0',command=lambda:bhan('0'))
bp=Button(mwin,text='+',command=lambda:bhan('+'))
bm=Button(mwin,text='-',command=lambda:bhan('-'))
be=Button(mwin,text='=',command=lambda:bhan('='))
bd=Button(mwin,text='.',command=lambda:bhan('.'))
bmu=Button(mwin,text='*',command=lambda:bhan('*'))
#bc=Button(mwin,text='',command=lambda:bhan(''))


e1.grid(row=0,column=0,columnspan=8)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b0.grid(row=4,column=1)
bd.grid(row=4,column=0)
bp.grid(row=1,column=3)
bm.grid(row=2,column=3)
bmu.grid(row=4,column=2)
#bc.grid(row=4,column=4)
be.grid(row=3,column=3,columnspan=2)

mwin.mainloop()

