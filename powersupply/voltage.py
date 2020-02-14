import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import threading

from tkinter import ttk
from tkinter import scrolledtext

from tkinter import scrolledtext
from scpi import *

# 设置仪器对象
m01 = Instrument(gpib_x, gpib_addr)

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('Setting')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

option2 = tk.LabelFrame(window, text="测量值", height=50, padx=10, pady=10)
option2.place(x=250, y=30, width=203)


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
    option1.place(x=20, y=30, width=180)
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

# Information = tk.LabelFrame(window, text="操作信息", padx=10, pady=10)
# Information.place(x=20, y=20)
# Information_Window = scrolledtext.ScrolledText(Information, width=20, height=5, padx=10, pady=10, wrap=tk.WORD)
# Information_Window.grid()
#
# Receive = tk.LabelFrame(window, text="接收区", padx=10, pady=10)  # 水平，垂直方向上的边距均为 10
# Receive.place(x=700, y=150)
# Receive_Window = scrolledtext.ScrolledText(Receive, width=20, height=12, padx=10, pady=10, wrap=tk.WORD)
# Receive_Window.grid()
#
# option = tk.LabelFrame(window, text="选项", padx=10, pady=10)
# option.place(x=20, y=400, width=203)
# # ************创建下拉列表**************
# ttk.Label(option, text="串口号:").grid(column=0, row=0)  # 添加串口号标签
# ttk.Label(option, text="波特率:").grid(column=0, row=1)  # 添加波特率标签
# ttk.Label(option, text="第三行").grid(column=0, row=2)  # 添加波特率标签
#
# Port = tk.StringVar()  # 端口号字符串
# Port_list = tk.Combobox(option, width=12, textvariable=Port, state='readonly')
# # ListPorts = list(serial.tool.list_ports.comports)  # 扫描当前可用串口保存到表ListPorts
# # Port_list['values'] = [i[0] for i in ListPorts]  # 下拉列表的值为ListPorts的所有值
# Port_list.current(0)  # 初始显示表中第一个值
# Port_list.grid(column=1, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行

# BaudRate = tk.StringVar()  # 波特率字符串
# BaudRate_list = tk.Combobox(option, width=12, textvariable=BaudRate, state='readonly')
# BaudRate_list['values'] = (1200, 2400, 4800, 9600, 14400, 19200, 38400, 43000, 57600, 76800, 115200)
# BaudRate_list.current(3)  # 初始显示9600
# BaudRate_list.grid(column=1, row=1)


# ######################电压设置
# var_voltage = tk.StringVar()
# var_voltage = tk.Entry(window, textvariable=var_voltage,width=10, font=('Arial', 14))
# var_voltage.place(x=95, y=3)
# #####################电流设置
# var_current = tk.StringVar()
# var_current = tk.Entry(window, textvariable=var_current,width = 10, font=('Arial', 14))
# var_current.place(x=95, y=63)

# # 第7步，login and sign up 按钮
# btn_login = tk.Button(window, text='Output Off', bg='red', command='none')
# btn_login.place(x=400, y=63)
#
# btn_login = tk.Button(window, text='Output On', bg='green', command='none')
# btn_login.place(x=400, y=3)
#######################*******************************************************************************************************************
# # 第5步，用户信息
# tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)
# tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)

# # 第6步，用户登录输入框entry
# # 用户名
# var_usr_name = tk.StringVar()
# var_usr_name.set('example@python.com')
# entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
# entry_usr_name.place(x=120, y=175)
# # 用户密码
# var_usr_pwd = tk.StringVar()
# entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
# entry_usr_pwd.place(x=120, y=215)


window.mainloop()
