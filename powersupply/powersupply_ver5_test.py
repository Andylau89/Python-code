import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import threading
import time
from tkinter import ttk
from tkinter import scrolledtext

from tkinter import scrolledtext
from scpi import *

channel_frame_width = 350
# 设置仪器对象
# m01 = Instrument(gpib_x, gpib_addr)
m01 = Instrument(0, 14)

# 下面指的set，设置值
channel_1_voltage = 0
channel_1_current = 0
channel_2_voltage = 0
channel_2_current = 0

# 下面指的读取值
read_channel_1_voltage = 0
read_channel_1_current = 0
read_channel_2_voltage = 0
read_channel_2_current = 0

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('HP6622A_Setting')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('800x600')  # 这里的乘是小x

# tk.Label(window, text='HP6622A Setting', font=('Arial', 16)).place(x=150, y=0)
tk.Label(window, text='HP6622A Setting', font=('Arial', 16)).pack()

channel_1 = tk.LabelFrame(window, text="Channel 1", padx=10, pady=10).pack()

channel_2 = tk.LabelFrame(window, text="Channel 2", padx=10, pady=10)
channel_2.place(x=400, y=350, width=channel_frame_width)

channel_1_protection = tk.LabelFrame(window, text="Channel_1_Protection", padx=10, pady=10)
channel_1_protection.place(x=20, y=110, width=channel_frame_width)

channel_2_protection = tk.LabelFrame(window, text="Channel_2_Protection", padx=10, pady=10)
channel_2_protection.place(x=400, y=110, width=channel_frame_width)

channel_1_status = tk.LabelFrame(window, text="Channel_1_Status", padx=10, pady=10)
channel_1_status.place(x=20, y=250, width=channel_frame_width)

channel_2_status = tk.LabelFrame(window, text="Channel_2_Status", padx=10, pady=10)
channel_2_status.place(x=400, y=250, width=channel_frame_width)

instrument_sta = tk.LabelFrame(window, text="Instrument Status", height=70, padx=10, pady=10)
instrument_sta.place(x=250, y=30, width=500)

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


# def output1():
#     channel_1_voltage = EntrySend_voltage1.get()
#     channel_1_current = EntrySend_current1.get()
#
#     channel_1_voltage = 'VSET 1 ' + channel_1_voltage
#     channel_1_current = 'ISET 1 ' + channel_1_current
#
#     m01.send(channel_1_voltage)
#     m01.send(channel_1_current)
#     m01.send('OUT 1,1')


def output2_on():
    channel_2_voltage = EntrySend_voltage2.get()
    channel_2_current = EntrySend_current2.get()

    channel_2_voltage = 'VSET 2 ' + channel_2_voltage
    channel_2_current = 'ISET 2 ' + channel_2_current

    m01.send(channel_2_voltage)
    m01.send(channel_2_current)

    m01.send('OUT 2,1')


def output2_off():
    m01.send('OUT 2,0')


def output1_on():
    channel_1_voltage = EntrySend_voltage1.get()
    channel_1_current = EntrySend_current1.get()

    channel_1_voltage = 'VSET 1 ' + channel_1_voltage
    channel_1_current = 'ISET 1 ' + channel_1_current

    m01.send(channel_1_voltage)
    m01.send(channel_1_current)

    m01.send('OUT 1,1')


def output1_off():
    m01.send('OUT 1,0')


def function_select():
    ####################################*************************************
    global EntrySend_voltage1, EntrySend_current1, EntrySend_voltage2, EntrySend_current2, EntrySend_voltage1_protection, EntrySend_current1_protection, EntrySend_voltage2_protection, EntrySend_current2_protection

    # scale_bar_1 = tk.LabelFrame(window, text="Scale", padx=10, pady=10)
    # scale_bar_1.place(x=300, y=100, width=100)
    #
    # tk.Scale(scale_bar_1, label='try me', from_=5, to=0, orient=tk.VERTICAL, length=400, showvalue=0, tickinterval=2,
    #          resolution=0.01, command='none').grid(column=0, row=0)

    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_voltage1 = tk.StringVar()
    # row 1
    tk.Label(channel_1, text='Voltage_Set:', font=('Arial', 10)).grid(column=1, row=0)
    vol_chan1 = ttk.Entry(channel_1, textvariable=EntrySend_voltage1, width=10).grid(column=2, row=0)
    # row 2
    tk.Label(channel_1, text='  ', font=('Arial', 10)).grid(column=1, row=1)
    # row 4
    tk.Label(channel_1, text='  ', font=('Arial', 10)).grid(column=1, row=4)

    # row 3
    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_current1 = tk.StringVar()
    tk.Label(channel_1, text='Current_Set:', font=('Arial', 10)).grid(column=1, row=2)
    cur_chan1 = ttk.Entry(channel_1, textvariable=EntrySend_current1, width=10).grid(column=2, row=2)

    tk.Label(channel_1, text='  ', font=('Arial', 10)).grid(column=1, row=3)

    # set_chan1_on = tk.Button(channel_1, text='Output_On', width=13, command=output1).grid(column=2, row=5)
    set_chan2_on = tk.Button(channel_1, text='Output_On', width=12, command=output1_on).grid(column=2, row=5)
    set_chan2_off = tk.Button(channel_1, text='Output_Off', width=12, command=output1_off).grid(column=4, row=5)
    ###########################################

    ####################################*************************************

    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_voltage2 = tk.StringVar()
    # row 1
    tk.Label(channel_2, text='Voltage_Set: ', font=('Arial', 10)).grid(column=1, row=0)
    vol_chan2 = ttk.Entry(channel_2, textvariable=EntrySend_voltage2, width=10).grid(column=2, row=0)
    # row 2
    tk.Label(channel_2, text='  ', font=('Arial', 10)).grid(column=1, row=1)
    # row 4
    tk.Label(channel_2, text='  ', font=('Arial', 10)).grid(column=1, row=4)

    # row 3
    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_current2 = tk.StringVar()
    tk.Label(channel_2, text='Current_Set: ', font=('Arial', 10)).grid(column=1, row=2)
    cur_chan1 = ttk.Entry(channel_2, textvariable=EntrySend_current2, width=10).grid(column=2, row=2)

    tk.Label(channel_2, text='  ', font=('Arial', 10)).grid(column=1, row=3)

    set_chan2_on = tk.Button(channel_2, text='Output_On', width=12, command=output2_on).grid(column=2, row=5)
    set_chan2_off = tk.Button(channel_2, text='Output_Off', width=12, command=output2_off).grid(column=4, row=5)

    ########################################################################################################################
    # channel1 over voltage set
    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_voltage1_protection = tk.StringVar()
    # row 1
    tk.Label(channel_1_protection, text='Over_Voltage_Set:', font=('Arial', 10)).grid(column=0, row=0)
    ttk.Entry(channel_1_protection, textvariable=EntrySend_voltage1_protection, width=10).grid(column=1, row=0)

    tk.Label(channel_1_protection, text='', font=('Arial', 10)).grid(column=0, row=1)

    # channel1 over current set
    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_current1_protection = tk.StringVar()
    # row 1
    tk.Label(channel_1_protection, text='Over_Current_Set:', font=('Arial', 10)).grid(column=0, row=2)
    ttk.Entry(channel_1_protection, textvariable=EntrySend_current1_protection, width=10).grid(column=1, row=2)
    clear_overprotection = tk.Button(channel_1_protection, text='Clear_OV', width=8,
                                     command=clear_channel1_over_protection).grid(column=3, row=2)
    set_overprotection = tk.Button(channel_1_protection, text='Confirm', width=8,
                                   command=set_channel1_over_protection).grid(column=3, row=0)

    #######################################################################################################################
    # channel2 over voltage set
    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_voltage2_protection = tk.StringVar()
    # row 1
    tk.Label(channel_2_protection, text='Over_Voltage_Set:', font=('Arial', 10)).grid(column=0, row=0)
    ttk.Entry(channel_2_protection, textvariable=EntrySend_voltage2_protection, width=10).grid(column=1, row=0)

    tk.Label(channel_2_protection, text='', font=('Arial', 10)).grid(column=0, row=1)

    # channel1 over current set
    DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
    EntrySend_current2_protection = tk.StringVar()
    # row 1
    tk.Label(channel_2_protection, text='Over_Current_Set:', font=('Arial', 10)).grid(column=0, row=2)
    ttk.Entry(channel_2_protection, textvariable=EntrySend_current2_protection, width=10).grid(column=1, row=2)
    clear_overprotection = tk.Button(channel_2_protection, text='Clear_OV', width=8,
                                     command=clear_channel2_over_protection).grid(column=3, row=2)
    set_overprotection = tk.Button(channel_2_protection, text='Confirm', width=8,
                                   command=set_channel2_over_protection).grid(column=3, row=0)


######################################Channel_1_status##################################################


def set_channel1_over_protection():
    value = EntrySend_voltage1_protection.get()
    cmd = 'OVSET1 ' + value
    m01.send(cmd)


def clear_channel1_over_protection():
    m01.send('OVSET1 50')
    m01.send('OVRST 1')


def set_channel2_over_protection():
    value = EntrySend_voltage2_protection.get()
    cmd = 'OVSET2 ' + value
    m01.send(cmd)


def clear_channel2_over_protection():
    m01.send('OVSET2 50')
    m01.send('OVRST 2')


function_select()


def get_voltage_current():
    m01.send('VOUT? 2')
    read_channel_1_voltage = m01.read()[:-2]

    m01.send('IOUT? 2')
    read_channel_1_current = m01.read()[:-2]

    tk.Label(channel_1, text=read_channel_1_voltage, font=('Arial', 10)).grid(column=1, row=0)
    tk.Label(channel_1, text=read_channel_1_current, font=('Arial', 10)).grid(column=2, row=0)

def get_channelx_status(x):
    cmd = 'STS?' + str(x)
    m01.send(cmd)
    sta_value_code = int(m01.read()[:-2])
    # print(sta_value_code)
    # print(sta_value_code)
    if  sta_value_code == 0:
        sta_value = 'Output_Off'
    elif sta_value_code == 1:
        sta_value = 'CV'

    elif sta_value_code == 2:
        sta_value = 'CC'

    elif sta_value_code == 8:
        sta_value = 'OV'

    else:
        sta_value = '未设置'
    return sta_value

def refresh_data():
    m01.send('VOUT? 2')
    read_channel_2_voltage = m01.read()[:-2]

    m01.send('IOUT? 2')
    read_channel_2_current = m01.read()[:-2]

    m01.send('VOUT? 1')
    read_channel_1_voltage = m01.read()[:-2]

    m01.send('IOUT? 1')
    read_channel_1_current = m01.read()[:-2]

    # m01.send('STS?2')
    # sta_value_code = int(m01.read()[:-2])
    # # print(sta_value_code)
    #
    # if sta_value_code == 1:
    #     sta_value = 'CV'
    #
    # elif sta_value_code == 2:
    #     sta_value = 'CC'
    #
    # elif sta_value_code == 3:
    #     sta_value = 'NONE'
    #
    # else:
    #     sta_value = 0
    sta_value_1 = get_channelx_status(1)
    sta_value_2 = get_channelx_status(2)

    tk.Label(channel_2, text=read_channel_2_voltage, bg='green', font=('Arial', 12)).grid(column=3, row=0)
    tk.Label(channel_2, text=read_channel_2_current, bg='yellow', font=('Arial', 12)).grid(column=3, row=2)

    tk.Label(channel_1, text=read_channel_1_voltage, bg='green', font=('Arial', 12)).grid(column=3, row=0)
    tk.Label(channel_1, text=read_channel_1_current, bg='yellow', font=('Arial', 12)).grid(column=3, row=2)


    # STATUS UPDATE
    tk.Label(instrument_sta, text=sta_value_1, bg='gray', font=('Arial', 12)).grid(column=3, row=2)

    tk.Label(channel_2_status, text='                              ',  font=('Arial', 12)).grid(column=0, row=0)
    tk.Label(channel_2_status, text=sta_value_2,  font=('Arial', 12)).grid(column=0, row=0)
    tk.Label(channel_1_status, text='                              ', font=('Arial', 12)).grid(column=0, row=0)
    tk.Label(channel_1_status, text=sta_value_1, font=('Arial', 12)).grid(column=0, row=0)



    window.after(100, refresh_data)  # 这里的10000单位为毫秒


refresh_data()
window.mainloop()
