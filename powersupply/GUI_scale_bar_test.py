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
m01 = Instrument(0, 14)
output = 0
# for i in range(30):
#     output += 0.1
#     output_cmd = 'VSET2 ' + str(output)
#     m01.send(output_cmd)

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1000x1000')  # 这里的乘是小x

# 第4步，在图形界面上创建一个标签label用以显示并放置
# l = tk.Label(channel_1, bg='green', fg='white', width=20, text='Channel_1_Voltage')
# l.pack()
#
# l2 = tk.Label(channel_1, bg='yellow', fg='black', width=20, text='Channel_1_Current')
# l2.pack()


# 第6步，定义一个触发函数功能
def vol_set_2(v):
    channel_1_V_read.config(text='Channel_1_Voltage: ' + v)
    output_cmd = 'VSET2 ' + v
    m01.send(output_cmd)

def cur_set_2(v):
    channel_1_I_read.config(text='Channel_1_Current: ' + v)
    output_cmd = 'ISET2 ' + v
    print(output_cmd)
    m01.send(output_cmd)


channel_1 = tk.LabelFrame(window, text="Channel 1", padx=10, pady=10)
channel_1.place(x=10, y=50, width=370)

channel_1_V_read = tk.Label(channel_1, bg='green', fg='white', width=20, text='Channel_1_Voltage')
channel_1_V_read.grid(column=0,row=0)

channel_1_I_read = tk.Label(channel_1, bg='green', fg='white', width=20, text='Channel_1_Current')
channel_1_I_read.grid(column=1,row=0)



# 第5步，创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
tk.Scale(channel_1, label='Voltage_Set',troughcolor='gray',bg='green', from_=5, to=0, orient=tk.VERTICAL, length=800, showvalue=1, tickinterval=2,
             resolution=0.01, command=vol_set_2).grid(column=0, row=1)

tk.Scale(channel_1, label='Current_Set', troughcolor='gray',bg='yellow',from_=4, to=0, orient=tk.VERTICAL, length=800, showvalue=1, tickinterval=2,
             resolution=0.001, command=cur_set_2).grid(column=1, row=1)


# 第7步，主窗口循环显示
window.mainloop()