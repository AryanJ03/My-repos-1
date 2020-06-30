import sys
from tkinter import *
A=int()
B=int()
C=int()
D=int()
def add():
    print("the two values you have entered are "+e1.get()+' and ' + e2.get())
    a=int(e1.get())
    b=int(e2.get())
    A=a+b
    print("the sum is: "+str(A))
    e3.insert(10, str(A))

def subtract():
    print("the 2 numbers are "+e1.get()+" and "+e2.get())
    a=int(e1.get())
    b=int(e2.get())
    B=a-b
    print('the difference is: '+str(B))
    e3.insert(10,str(B))
    
def multiplication():
    print('the 2 numbers you have entered are: '+e2.get()+' and '+e1.get())
    a= int(e1.get())
    b= int(e2.get())
    C=a*b
    print('the product is: '+str(C))
    e3.insert(10, str(C))
    
    
def division():
    print('the 2 numbers you have entered are: '+e1.get()+' and '+e2.get())
    a=int(e1.get())
    b=int(e2.get())
    D=a/b
    print('the quotient is: '+str(D))
    e3.insert(10, str(D))


def percentage():
    print('the 2 numbers you have entered is '+e1.get()+' and '+e2.get())
    a=int(e1.get())
    b=int(e2.get())
    A=a/b*100
    print("the pecentage is:"+str(A))
    e3.insert(10, str(A))

def square():
    print('the number you have entered is '+e1.get())
    a=int(e1.get())
    A=a*a
    print('the square of the number is:'+str(A))
    e3.insert(10, str(A))


def cube():
    print('the number you have entered is:'+e1.get())
    a=int(e1.get())
    A=a*a*a
    print('the cube is:'+str(A))
    e3.insert(10, str(A))

def AC():
    print('all the values are cleared')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

def one():
    print('one has been inserted')
    A=1
    e1.insert(10, int(A))

def two():
    print('two has been iserted')
    A=2
    e1.insert(10, int(A))

def three():
    print('three has been inserted')
    A=3
    e1.insert(10, int(A))

def four():
    print('four has been iserted')
    A=4
    e1.insert(10, int(A))

def five():
    print('five has been inserted')
    A=5
    e1.insert(10, int(A))


def six():
    print('six has been inserted')
    A=6
    e1.insert(10, int(A))

def seven():
    print('seven has been inserted')
    A=7
    e1.insert(10, int(A))

def eight():
    print('eight has been inserted')
    A=8
    e1.insert(10, int(A))

def nine():
    print('nine has been inserted')
    A=9
    e1.insert(10, int(A))

def zero():
    print('zero has been inserted')
    A=0
    e1.insert(10, int(A))
    
def one2():
    print('one has been inserted in 2nd')
    A=1
    e2.insert(10, int(A))

def two2():
    print('two has been iserted in 2nd')
    A=2
    e2.insert(10, int(A))

def three2():
    print('three has been inserted in 2nd')
    A=3
    e2.insert(10, int(A))

def four2():
    print('four has been iserted in 2nd')
    A=4
    e2.insert(10, int(A))

def five2():
    print('five has been inserted in 2nd')
    A=5
    e2.insert(10, int(A))

def six2():
    print('six has been inserted in 2nd')
    A=6
    e2.insert(10, int(A))

def seven2():
    print('seven has been inserted in 2nd')
    A=7
    e2.insert(10, int(A))

def eight2():
    print('eight has been inserted in 2nd')
    A=8
    e2.insert(10, int(A))

def nine2():
    print('nine has been inserted in 2nd')
    A=9
    e2.insert(10, int(A))

def zero2():
    print('zero has been inserted in 2nd')
    A=0
    e2.insert(10, int(A))
    
def sin0():
    print('sin (0)=0')
    A=0
    e3.insert(10, str(A))
def sin30():
    print('sin(30)=1/2')
    A='1/2'
    e3.insert(10, str(A))

def sin60():
    print('sin(60)=root_3/2')
    A='root_3/2'
    e3.insert(10, str(A))

def sin45():
    print('sin(45)=root_2/2')
    A='root_2/2'
    e3.insert(10, str(A))

def sin90():
    print('sin(90)=1')
    A=1
    e3.insert(10, str(A))

def cos0():
    print('cos(0)=1')
    A=1
    e3.insert(10, str(A))

def cos30():
    print('cos(30)=root_3/2')
    A='root_3/2'
    e3.insert(10, str(A))

def cos45():
    print('cos(45)=root_2/2')
    A='root_2/2'
    e3.insert(10, str(A))

def cos60():
    print('cos(60)=1/2')
    A='1/2'
    e3.insert(10, str(A))

def cos90():
    print('cos(90)=0')
    A=0
    e3.insert(10, str(A))

#this is where you declare a frame 

frame=Tk()
frame.title('my first GUI calculator \a')
frame.geometry('1025x300')

#this is the text which will appear on the main frame
Label(frame, text="1st no.").grid(row=0)
Label(frame, text="2nd no.").grid(row=1)
Label(frame, text="Answer").grid(row=3)
Label(frame, text='Note: Use only first box saying"first number" for squaring and cubing').grid(row=7, column=0)


#this function lets you enter the value in your boxes


e1=Entry(frame)
e2=Entry(frame)
e3=Entry(frame)

#this is where you define the place on the frmae for your data entry

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=3, column=1)

#this function shows the buttons on the frame 

Button(frame, text='sin 0', command=sin0).grid(row=11, column=13)
Button(frame, text='sin 30', command=sin30).grid(row=11, column=12)
Button(frame, text='sin 45', command=sin45).grid(row=11, column=11)
Button(frame, text='sin 60', command=sin60).grid(row=11, column=10)
Button(frame, text='sin 90', command=sin90).grid(row=11, column=9)

Button(frame, text='cos 0', command=cos0).grid(row=11, column=8)
Button(frame, text='cos 30', command=cos30).grid(row=11, column=7)
Button(frame, text='cos 45', command=cos45).grid(row=11, column=6)
Button(frame, text='cos 60', command=cos60).grid(row=11, column=5)
Button(frame, text='cos 90', command=cos90).grid(row=11, column=4)

Button(frame, text='add', command=add).grid(row=2, column=1)
Button(frame, text='subtract', command=subtract).grid(row=2, column=2)
Button(frame, text='multiply', command=multiplication).grid(row=2, column=3)
Button(frame, text='divide', command=division).grid(row=2, column=4)
Button(frame, text='percentage', command=percentage).grid(row=2, column=5)
Button(frame, text='square', command=square).grid(row=2, column=6)
Button(frame, text='cube', command=cube).grid(row=5, column=1)
Button(frame, text='all clear', command=AC).grid(row=0, column=3)

Button(frame, text='1[1st no.]', command=one).grid(row=8, column=0)
Button(frame, text='2[1st no.]', command=two).grid(row=8, column=1)
Button(frame, text='3[1st no.]', command=three).grid(row=8, column=2)
Button(frame, text='4[1st no.]', command=four).grid(row=8, column=3)
Button(frame, text='5[1st no.]', command=five).grid(row=8, column=4)
Button(frame, text='6[1st no.]', command=six).grid(row=8, column=5)
Button(frame, text='7[1st no.]', command=seven).grid(row=9, column=0)
Button(frame, text='8[1st no.]', command=eight).grid(row=9, column=1)
Button(frame, text='9[1st no.]', command=nine).grid(row=9, column=2)
Button(frame, text='0[1st no.]', command=zero).grid(row=9, column=3)

Button(frame, text='1[2nd no.]', command=one2).grid(row=9, column=4)
Button(frame, text='2[2nd no.]', command=two2).grid(row=9, column=5)
Button(frame, text='3[2nd no.]', command=three2).grid(row=10, column=0)
Button(frame, text='4[2nd no.]', command=four2).grid(row=10, column=1)
Button(frame, text='5[2nd no.]', command=five2).grid(row=10, column=2)
Button(frame, text='6[2nd no.]', command=six2).grid(row=10, column=3)
Button(frame, text='7[2nd no.]', command=seven2).grid(row=10, column=4)
Button(frame, text='8[2nd no.]', command=eight2).grid(row=10, column=5)
Button(frame, text='9[2nd no.]', command=nine2).grid(row=11, column=0)
Button(frame, text='0[2nd no.]', command=zero2).grid(row=11, column=1)
print(sys.version)
mainloop()
