import tkinter as tk  # 使用Tkinter前需要先导入

import numpy as np
import matplotlib.pyplot as plt
from threading import Thread
from matplotlib.widgets import Button

from time import sleep

from scpi import *
m01 = Instrument(0, 7)

test = '''
    *RST
    AUTOSCALE
    # measure:freq?
    # measure:vpp?    
    acquire:type normal
    acquire:points 1000
    acquire:complete 500
    digitize channel 1
    
    '''
test01 = '''
    WAVEFORM:FORMAT WORD
    WAVEFORM:FORMAT ASCII
    WAVEFORM:PREAMBLE?
    WAVEFORM:DATA?

'''

fig, ax = plt.subplots()
# 设置图形显示位置
plt.subplots_adjust(bottom=0.2)


print(m01.send(test01))
str01 = m01.query('WAVEFORM:DATA?')
y = str01.split(',')
# print(y)
# print(type(y[0]))
# print(type(list))
y01 = []
for item in y:
    y01.append(int(item))
# print(444444444444444444455555555555555)
# print(y01)
# print(type(y01[0]))
# print(len(y))


# plt.plot(0,list[0],'o')
# plt.plot(1,list[1],'o')
# plt.plot(2,list[2],'o')
# plt.plot(3,list[3],'o')

# for x in range(500):
#     plt.plot(x,list[x],'o')

list_x = []
for i in range(500):
    list_x.append(i)

# x = [1,2,3,4,5,6,7,8]
print('max',max(y01))
print('min',min(y01))



l, = plt.plot(list_x,y01)


# 自定义类，用来封装两个按钮的单击事件处理函数
class ButtonHandler:
    def __init__(self):
        self.flag = True
        # self.range_s, self.range_e, self.range_step = 0, 1, 0.005
    # 线程函数，用来更新数据并重新绘制图形


    def threadStart(self):
        while self.flag:
            sleep(0.02)

            list_x = []
            for i in range(500):
                list_x.append(i)

            str01 = m01.query('WAVEFORM:DATA?')
            y = str01.split(',')
            y01 = []
            for item in y:
                y01.append(int(item))


            l.set_ydata(y01)
            l.set_xdata(list_x)
            plt.grid(linestyle='-.')
            plt.draw()


    def Start(self, event):
        self.flag = True
        # 创建并启动新线程
        t = Thread(target=self.threadStart)
        t.start()


    def Stop(self, event):
        self.flag = False


callback = ButtonHandler()


axprev = plt.axes([0.81, 0.0, 0.1, 0.075])
bprev = Button(axprev, 'Stop')
bprev.on_clicked(callback.Stop)
axnext = plt.axes([0.7, 0.0, 0.1, 0.075])
bnext = Button(axnext, 'Start')
bnext.on_clicked(callback.Start)

plt.grid(linestyle='-.')

plt.show()



# print(m01.query('measure:freq?'))
# print(m01.query('measure:VPP?'))
# print(m01.send(test))
