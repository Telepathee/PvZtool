import tkinter as tk
import pymem as pm
from tkinter import *

# 可能需要修改进程名称
process_pvz = pm.Pymem('PlantsVsZombies.exe')
module_pvz = pm.process.module_from_name(process_pvz.process_handle, 'PlantsVsZombies.exe')
root_address = pm.memory.read_int(process_pvz.process_handle, module_pvz.lpBaseOfDll + 0x2A9EC0)

window = tk.Tk()
window.title('植物大战僵尸修改')
window.geometry('500x300')

value_sun = StringVar()

#########################################################################################
# 修改阳光
# 偏移1：0x5560
sun_offset1 = 0x5560

# 偏移2：0x768
sun_offset2 = 0x768


def writesun1():
    number = sun.get()
    if number != '':
        whitesun2(int(number))


def whitesun2(number):
    sunaddr = pm.memory.read_int(process_pvz.process_handle, root_address + sun_offset2)
    process_pvz.write_int(sunaddr + sun_offset1, int(number))


def readsun():
    sun.delete(0, 'end')
    sun_value = process_pvz.read_int(pm.memory.read_int(process_pvz.process_handle,
                                                        root_address + sun_offset2) + sun_offset1)
    sun.insert(0, str(sun_value))


def writesun3():
    sunaddr = pm.memory.read_int(process_pvz.process_handle, root_address + sun_offset2)
    process_pvz.write_int(sunaddr + sun_offset1, 99999)


sun_tip = tk.Label(window, text="阳光：")
sun_tip.place(relx=0.05, rely=0.05)

sun = tk.Entry(window)
sun.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.08)

read_sun = tk.Button(window, text="读取值", command=readsun)
read_sun.place(relx=0.4, rely=0.05, relwidth=0.15, relheight=0.1)

write_sun = tk.Button(window, text="修改", command=writesun1)
write_sun.place(relx=0.6, rely=0.05, relwidth=0.15, relheight=0.1)

write_sun = tk.Button(window, text="无限阳光", command=writesun3)
write_sun.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.1)

#########################################################################################
# 修改金币
# 偏移1：0x28
coin_offset1 = 0x28

# 偏移2：0x82C
coin_offset2 = 0x82C


def whitecoin2(number):
    coinaddr = pm.memory.read_int(process_pvz.process_handle, root_address + coin_offset2)
    process_pvz.write_int(coinaddr + coin_offset1, int(number))


def writecoin1():
    number = coin.get()
    if number != '':
        whitecoin2(int(number))


def readcoin():
    coin.delete(0, 'end')
    coin_value = process_pvz.read_int(pm.memory.read_int(process_pvz.process_handle,
                                                         root_address + coin_offset2) + coin_offset1)
    coin.insert(0, str(coin_value))


def writecoin3():
    coinaddr = pm.memory.read_int(process_pvz.process_handle, root_address + coin_offset2)
    process_pvz.write_int(coinaddr + coin_offset1, 99999)


coin_tip = tk.Label(window, text="金币：")
coin_tip.place(relx=0.05, rely=0.25)

x10 = tk.Label(window, text="0")
x10.place(relx=0.33, rely=0.25)

coin = tk.Entry(window)
coin.place(relx=0.13, rely=0.25, relwidth=0.2, relheight=0.08)

read_coin = tk.Button(window, text="读取值", command=readcoin)
read_coin.place(relx=0.4, rely=0.25, relwidth=0.15, relheight=0.1)

write_coin = tk.Button(window, text="修改", command=writecoin1)
write_coin.place(relx=0.6, rely=0.25, relwidth=0.15, relheight=0.1)

write_coin = tk.Button(window, text="无限金币", command=writecoin3)
write_coin.place(relx=0.8, rely=0.25, relwidth=0.15, relheight=0.1)

#####################################################################################
# 修改关卡
# 偏移1：0x24
level_offset1 = 0x24

# 偏移2：0x82C
level_offset2 = 0x82C


def change1(number):
    if number % 10 == 0:
        x = number // 10
        y = 10
    else:
        x = number // 10 + 1
        y = number % 10
    return [x, y]


def change2(x, y):
    if y == 10:
        return x * 10
    else:
        return (x - 1) * 10 + y


def writelevel():
    x = int(ccount.get())
    y = int(gcount.get())
    number = change2(x, y)

    leveladdr = pm.memory.read_int(process_pvz.process_handle, root_address + level_offset2)
    process_pvz.write_int(leveladdr + level_offset1, number)


def readlevel():
    level = process_pvz.read_int(pm.memory.read_int(process_pvz.process_handle,
                                                    root_address + level_offset2) + level_offset1)
    ccount.delete(0, 'end')
    gcount.delete(0, 'end')
    x, y = change1(level)
    ccount.insert(0, str(x))
    gcount.insert(0, str(y))


level_tip = tk.Label(window, text="关卡：")
level_tip.place(relx=0.05, rely=0.45)
# 文字打印
di1 = tk.Label(window, text="第")
di1.place(relx=0.13, rely=0.45)
ceng = tk.Label(window, text="层,")
ceng.place(relx=0.28, rely=0.45)
di2 = tk.Label(window, text="第")
di2.place(relx=0.32, rely=0.45)
guan = tk.Label(window, text="关")
guan.place(relx=0.47, rely=0.45)
# 层&关
ccount = tk.Entry(window)
ccount.place(relx=0.17, rely=0.45, relwidth=0.1, relheight=0.08)
gcount = tk.Entry(window)
gcount.place(relx=0.36, rely=0.45, relwidth=0.1, relheight=0.08)
# 按钮
read_level = tk.Button(window, text="读取值", command=readlevel)
read_level.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)

write_level = tk.Button(window, text="修改", command=writelevel)
write_level.place(relx=0.8, rely=0.45, relwidth=0.15, relheight=0.1)

window.mainloop()
