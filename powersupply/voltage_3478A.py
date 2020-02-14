import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import threading

from tkinter import ttk
from tkinter import scrolledtext

from tkinter import scrolledtext
from scpi import *

# 设置仪器对象
# m01 = Instrument(gpib_x, gpib_addr)

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('DMM_3478A_Setting')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x350')  # 这里的乘是小x

tk.Label(window, text='Measuring Mode', font=('Arial', 16)).place(x=150, y=0)

option2 = tk.LabelFrame(window, text="测量值", height=50, padx=10, pady=10)
option2.place(x=250, y=30, width=203)

gpib_position = tk.LabelFrame(window, text="GPIB_Address", height=60, padx=10, pady=10)
gpib_position.place(x=20, y=30, width=180)
tk.Label(gpib_position, text='GPIB', font=('Arial', 10)).grid(column=0, row=0)

DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
EntrySend = tk.StringVar()
Send_Window = ttk.Entry(gpib_position, textvariable=EntrySend, width=2).grid(column=1, row=0)
tk.Label(gpib_position, text='::', font=('Arial', 10)).grid(column=2, row=0)
# tk.Label(gpib_position, text='ADDR', font=('Arial', 10)).grid(column=2, row=0)

DataSend1 = tk.StringVar()
EntrySend1 = tk.StringVar()
Send_Window1 = ttk.Entry(gpib_position, textvariable=EntrySend1, width=2).grid(column=4, row=0)


def set_gpib_addr():
    global DataSend
    global DataSend1
    global m01
    gpib_x = EntrySend.get()
    gpib_addr = EntrySend1.get()
    m01 = Instrument(int(gpib_x), int(gpib_addr))

    # print(gpib_addr)
    # print(gpib_x)

tk.Label(gpib_position, text='::INST', font=('Arial', 10)).grid(column=5, row=0)
gpib_select = tk.Button(gpib_position, text='确认', width=3, bg='green', command=set_gpib_addr).grid(column=6, row=0)



# tk.Label(window, text='Voltage', font=('Arial', 16)).pack()
# tk.Label(window, text=m01.read(), font=('Arial', 10)).place(x=10, y=0)
# tk.Label(window, text=m01.read(), bg='yellow', font=('Arial', 10)).place(x=10, y=120)

def read_data():
    # m01.read()[:-2]删除读出来的最后两位，因为是回车两行，所以删除
    tk.Label(option2, text=m01.read()[:-2], bg='yellow', font=('Arial', 10)).grid(column=2, row=0)


def set_DC_Voltage():
    m01.send('F1')
    tk.Label(window, text='DC_Voltage Mode', font=('Arial', 16)).place(x=150, y=0)


def set_AC_Voltage():
    m01.send('F2')
    tk.Label(window, text='AC_Voltage Mode', font=('Arial', 16)).place(x=150, y=0)


def set_DC_Current():
    m01.send('F5')
    tk.Label(window, text='DC_Current Mode', font=('Arial', 16)).place(x=150, y=0)


def set_AC_Current():
    m01.send('F6')
    tk.Label(window, text='AC_Current Mode', font=('Arial', 16)).place(x=150, y=0)


def set_2w_ohms():
    m01.send('F3')
    tk.Label(window, text='Ohms-2wire Mode', font=('Arial', 16)).place(x=150, y=0)


def set_4w_ohms():
    m01.send('F4')
    tk.Label(window, text='Ohms-4wire Mode', font=('Arial', 16)).place(x=150, y=0)


def function_select():
    global btn_login
    option1 = tk.LabelFrame(window, text="设置", padx=10, pady=10)
    option1.place(x=20, y=100, width=180)
    btn_login = tk.Button(option1, text='DC Voltage', width=15, bg='green', command=set_DC_Voltage)
    btn_login.grid(column=0, row=0)
    btn_login = tk.Button(option1, text='AC Voltage', width=15, bg='green', command=set_AC_Voltage)
    btn_login.grid(column=0, row=1)
    btn_login = tk.Button(option1, text='DC Current', width=15, bg='green', command=set_DC_Current)
    btn_login.grid(column=0, row=2)
    btn_login = tk.Button(option1, text='AC Current', width=15, bg='green', command=set_AC_Current)
    btn_login.grid(column=0, row=3)
    btn_login = tk.Button(option1, text='2-Wire Ohms', width=15, bg='green', command=set_2w_ohms)
    btn_login.grid(column=0, row=4)
    btn_login = tk.Button(option1, text='4-Wire Ohms', width=15, bg='green', command=set_4w_ohms)
    btn_login.grid(column=0, row=5)


function_select()

btn_login = tk.Button(option2, text='read', width=8, bg='yellow', command=read_data)
btn_login.grid(column=0, row=0)

window.mainloop()
