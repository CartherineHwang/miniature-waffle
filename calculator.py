# -*- coding: utf-8 -*-
"""
Created on Wed May 17 00:21:37 2023

@author: HFY
"""

import tkinter as tk
###制作一个窗口，这就是计算器的壳子
root = tk.Tk()
root.geometry("300x300+150+150")
root.title('calculator')
root.attributes("-alpha", 0.9)
root["background"] = "#ffffff"
###建立列表收集输入
lists = []
result_num = tk.StringVar()
result_num.set(0)


###显示数字
def append_num(i):
    lists.append(i)
    result_num.set(''.join(lists))
    
###进行符号运算
def operator(i):
    if len(lists) > 0:
        if lists[-1] in ['+', '-', '*', '/']:
            lists[-1] = i
        else:
            lists.append(i)
        result_num.set(''.join(lists))
        
###等于号
def equal():
    a = ''.join(lists)
    end_num = eval(a)
    result_num.set(end_num)
    lists.clear()
    lists.append(str(end_num))
    result_num.set(lists)
    
###清空
def clear():
    lists.clear()
    result_num.set(0)

###返回
def back():
    lists.pop()
    result_num.set(lists)
    

###按钮界面设置
lable1 = tk.Label(root, textvariable=result_num, width=20, height=2, font=('宋体', 20), justify='left', background='#ffffff', anchor='se')
lable1.grid(padx=4, pady=4, row=0, column=0, columnspan=4)

button_clear = tk.Button(root, text='C', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: clear())
button_back = tk.Button(root, text='←', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: back())
button_division = tk.Button(root, text='/', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('/'))
button_multiplication = tk.Button(root, text='x', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('*'))
button_clear.grid(padx=4, row=1, column=0)
button_back.grid(padx=4, row=1, column=1)
button_division.grid(padx=4, row=1, column=2)
button_multiplication.grid(padx=4, row=1, column=3)

button_seven = tk.Button(root, text='7', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('7'))
button_eight = tk.Button(root, text='8', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('8'))
button_nine = tk.Button(root, text='9', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('9'))
button_subtraction = tk.Button(root, text='—', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('-'))
button_seven.grid(padx=4, row=2, column=0)
button_eight.grid(padx=4, row=2, column=1)
button_nine.grid(padx=4, row=2, column=2)
button_subtraction.grid(padx=4, row=2, column=3)

button_four = tk.Button(root, text='4', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('4'))
button_five = tk.Button(root, text='5', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('5'))
button_six = tk.Button(root, text='6', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('6'))
button_addition = tk.Button(root, text='+', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('+'))
button_four.grid(padx=4, row=3, column=0)
button_five.grid(padx=4, row=3, column=1)
button_six.grid(padx=4, row=3, column=2)
button_addition.grid(padx=4, row=3, column=3)

button_one = tk.Button(root, text='1', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('1'))
button_two = tk.Button(root, text='2', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('2'))
button_three = tk.Button(root, text='3', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('3'))
button_equal = tk.Button(root, text='=', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: equal())
button_one.grid(padx=4, row=4, column=0)
button_two.grid(padx=4, row=4, column=1)
button_three.grid(padx=4, row=4, column=2)
button_equal.grid(padx=4, row=4, column=3)

button_zero = tk.Button(root, text='0', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('0'))
button_point = tk.Button(root, text='.', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('.'))
button_leftparentese= tk.Button(root, text='(', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('('))
button_rightparentese= tk.Button(root, text=')', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num(')'))
button_zero.grid(padx=4, row=5, column=1)
button_point.grid(padx=4, row=5, column=0)
button_leftparentese.grid(padx=4, row=5, column=2)
button_rightparentese.grid(padx=4, row=5, column=3)
root.mainloop()











