# 重要：不能安装visa，只能安装pyvisa. 也就是只 pip install pyvisa
#       千万不要pip install visa，如果装了，import pyvisa as visa。。。。浪费了一天。。。

# import pyvisa as visa
import visa
# from CMD_define_33522B import *

set_form = """
    FUNCtion SQU
    FREQuency +1.0E+04
    VOLTage +1
    VOLTage:OFFset 0.0
    AM:SOURce INT
    AM:DSSC 0
    AM:DEPTh +120
    AM:INTernal:FUNCtion TRI
    AM:INTernal:FREQ 5E+02
    AM:STATe 1
    OUTPut1 1
"""



set_sin = """
    FUNCtion SIN
    FREQuency +1.0E+05
    VOLTage:HIGH +2.0
    VOLTage:LOW +0.0
    OUTPut ON
    PHASe +90.0


"""

set_square = """
    FUNC SQU
    FUNC:SQU:DCYC +20.0
    FREQ +1.0E+04
    VOLT:HIGH +4.0
    VOLT:LOW -1.0
    OUTP 1
"""

set_ramp = """
    FUNCtion RAMP
    FUNCtion:RAMP:SYMMetry 25
    FREQ +1.0E+03
    VOLTage +2.0
"""

set_pulse = """
    FUNC PULS
    FUNC:PULS:TRAN:LEAD 4E-8
    FUNC:PULS:TRAN:TRA 1E-6
    FUNC:PULS:WIDT 3E-6
    FREQ 2E5
    VOLT 3
    OUTP ON
"""

set_listfreq = """
    FUNCtion SQU
    TRIGger:SOURce IMMediate
    FREQuency:MODE LIST
    LIST:DWELl +5.0E-03
    LIST:FREQuency +1.0E+03,+3.0E+03,+7.0E+03
    VOLTage +1.0
    OUTPut 1
"""

set_arbitrary = """
    UNCtion ARB
    VOLTage +3
    VOLTage:OFFSet +1
    FUNC:ARB:SRAT 1E5
    FUNCtion:ARBitrary "INT:\BUILTIN\EXP_RISE.ARB"
    OUTPut 1

"""

output_1_on = 'OUTPut1 1'
output_1_off = 'OUTPut1 0'
output_2_on = 'OUTPut2 1'
output_2_off = 'OUTPut2 0'

visa_dll = 'c:/windows/system32/visa32.dll'


class Instrument:
    def __init__(self, gpib_addr):
        self.visaDLL = 'c:/windows/system32/visa32.dll'
        self.address = 'GPIB0::%d::INSTR' % (gpib_addr)
        self.resourceManager = visa.ResourceManager(self.visaDLL)
        self.instance = self.resourceManager.open_resource(self.address)

    def open(self):
        # self.instance = self.resourceManager.open_resource(self.address)
        self.idn = self.instance.query('*IDN?')
        print(self.idn)

    def query(self, data):
        # self.instance = self.resourceManager.open_resource(self.address)
        self.idn = self.instance.query(data)
        print(self.idn)

    def reset(self):
        # self.instance = self.resourceManager.open_resource(self.address)
        self.instance.write('*RST')

    def close(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None

    def send(self, cmd):
        self.instance.write(cmd)

    def set_freq(self, value):
        cmd_set = 'FREQuency ' + str(value)
        self.send(cmd_set)

    def set_votage(self, value):
        cmd_set = 'VOLTage ' + str(value)
        self.send(cmd_set)

    def set_waveform(self, value):
        cmd_setfre = 'FREQuency ' + str(value)
        self.send(cmd_setfre)

    def read(self):
        return self.instance.read()


if __name__ == '__main__':
    m01 = Instrument(10)
    # m01.open()
    # m01.open()
    # m01.query('*IDN?')
    # m01.reset()
    # m01.send(output_1_on)
    # m01.send(output_2_off)
    # m01.send('FREQuency +1.0E+04')
    # m01.set_freq(8000)
    # m01.set_votage(0.9)
    # m01.send(set_form)
    # m01.close()
    m01.reset()
    # m01.set_freq('10khz')
    # m01.set_votage('1v')

    # m01.send('FUNCtion SQU')
    # m01.send('FUNCtion SIN')
    # m01.send('FUNCtion RAMP')
    # m01.send(set_form)
    # m01.reset()
    #
    # m01.send(set_square)
    while True:
        a = int(input("请输入数字1-7："))
        m01.reset()
        if a == 1:
            m01.send(set_form)
        elif a == 2:
            m01.send(set_sin)

        elif a == 3:
            m01.send(set_square)

        elif a == 4:
            m01.send(set_ramp)

        elif a == 5:
            m01.send(set_pulse)

        elif a == 6:
            m01.send(set_listfreq)

        elif a == 7:
            m01.send(set_arbitrary)

    # m01.close()

# m01.close()

# a = visa.ResourceManager().list_resources()
# print(visa.ResourceManager().list_resources())
# print(type(a))
# for item in a:
#     if item[0:4] == 'GPIB':
#         gpibadd = item[4]
#         print('GPIB端口是: ' + gpibadd)
#         print("*******")
#     print(item)


#
#     rm = visa.ResourceManager(visa_dll)
#     self.ser = rm.open_resource(self.gpibaddr)
#
# def Write(self, data):
#     self.ser.write(data)
#
# def Set_DC(self, data=10):
#     self.Write("CONF:CURR:DC " + str(data))
#
# def Set_AC(self, data=10):
#     self.Write("CONF:CURR:AC " + str(data))
#
# def Read_IC(self):
#     return float(self.ser.query("READ?"))
#
# def Read(self):
#     return self.ser.read()
#
