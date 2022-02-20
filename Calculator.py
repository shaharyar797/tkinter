from tkinter import *

root = Tk()

root.title("Calculator")
    

entry_box = Entry(root,width=35,font=('Century Schoolbook', 12))
entry_box.grid(row=0,column=0,columnspan=4,padx=10,pady=20,ipady=5)

answer = 0
val1=""

operands=['+','-','*','/','=']

def button_click(number):
    current = entry_box.get()
    if number in operands:
        if current[-1] not in operands:
            entry_box.delete(0,END)
            entry_box.insert(0,str(current)+str(number))
    
    elif number == '.':
        flag = 1
        l = len(current)
        i = -1
        while(i>=-l):
            if current[i] == '.':
                flag = 0
                break
            elif current[i] in operands:
                flag = 1
                break
            i=i-1
        if(flag == 1):
            entry_box.delete(0,END)
            entry_box.insert(0,str(current)+str(number))
    
    else:
        entry_box.delete(0,END)
        entry_box.insert(0,str(current)+str(number))
    
def button_clear():
    entry_box.delete(0,END)
    
#def operations(op):    
             
                
    
def button_equal():
    current = entry_box.get()
    if current[-1] not in operands:
        entry_box.delete(0,END)
        entry_box.insert(0,str(current)+"=")
        current = entry_box.get()
        op = '+'
        val1=""
        answer=0.00
        for i in range(len(current)):
            if current[i] in operands:
                if op == '+':
                    answer = answer + float(val1)
                if op == '-':
                    answer = answer - float(val1)
                if op == '*':
                    answer = answer * float(val1)
                if op == '/':
                    answer = answer / float(val1)
                val1="" 
                op = current[i]
            else:
                val1 = val1 + current[i]
            i=i+1
        entry_box.delete(0,END)
        entry_box.insert(0,answer)
        
def button_back():
    current=entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0,current[0:-1])
    
#def operations:
    
    

back_button = Button(root,text="←",width=20,height=2,command=button_back)
back_button.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

clear_button = Button(root,text="Clear",width=20,height=2,command=button_clear)
clear_button.grid(row=1,column=2,columnspan=2,padx=5,pady=5)

button_7 = Button(root,text="7",width=7,height=2,command=lambda:button_click(7))
button_7.grid(row=2,column=0,padx=5,pady=5)

button_8 = Button(root,text="8",width=7,height=2,command=lambda:button_click(8))
button_8.grid(row=2,column=1,padx=5,pady=5)

button_9 = Button(root,text="9",width=7,height=2,command=lambda:button_click(9))
button_9.grid(row=2,column=2,padx=5,pady=5)

button_add = Button(root,text="+",width=7,height=2,command=lambda:button_click('+'))
button_add.grid(row=2,column=3,padx=5,pady=5)

button_4 = Button(root,text="4",width=7,height=2,command=lambda:button_click(4))
button_4.grid(row=3,column=0,padx=5,pady=5)

button_5 = Button(root,text="5",width=7,height=2,command=lambda:button_click(5))
button_5.grid(row=3,column=1,padx=5,pady=5)

button_6 = Button(root,text="6",width=7,height=2,command=lambda:button_click(6))
button_6.grid(row=3,column=2,padx=5,pady=5)

button_sub = Button(root,text="-",width=7,height=2,command=lambda:button_click('-'))
button_sub.grid(row=3,column=3,padx=5,pady=5)

button_1 = Button(root,text="1",width=7,height=2,command=lambda:button_click(1))
button_1.grid(row=4,column=0,padx=5,pady=5)

button_2 = Button(root,text="2",width=7,height=2,command=lambda:button_click(2))
button_2.grid(row=4,column=1,padx=5,pady=5)

button_3 = Button(root,text="3",width=7,height=2,command=lambda:button_click(3))
button_3.grid(row=4,column=2,padx=5,pady=5)

button_mul = Button(root,text="*",width=7,height=2,command=lambda:button_click('*'))
button_mul.grid(row=4,column=3,padx=5,pady=5)

button_0 = Button(root,text="0",width=20,height=2,command=lambda:button_click(0))
button_0.grid(row=5,column=0,columnspan=2,padx=5,pady=5)

button_dec = Button(root,text=".",width=7,height=2,command=lambda:button_click("."))
button_dec.grid(row=5,column=2,padx=5,pady=5)

button_div = Button(root,text="/",width=7,height=2,command=lambda:button_click('/'))
button_div.grid(row=5,column=3,padx=5,pady=5)

button_equal = Button(root,text="=",width=43,height=2,command=button_equal)
button_equal.grid(row=6,column=0,columnspan=4,padx=5,pady=5)

root.mainloop()