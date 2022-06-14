from msilib.schema import RadioButton
import tkinter
from tkinter import *
from turtle import update
from pypresence import Presence
import time

from uritemplate import variables


def update():

    f = open("discord_rpc.txt", 'w')

    client_id1 = client_id.get()
    state1 = state.get()
    details1 = details.get()

    f.write(client_id1 + "," + state1 + "," + details1)
    f.close()


def start():
    f = open("discord_rpc.txt", 'r')
    line = f.readline()
    print(line)
    line = line.split(",")
    client_id1 = line[0]
    try:
        RPC = Presence(client_id=client_id1)
        RPC.connect()
    except:
        messagebox.showwarning("오류", "잘못된 client_id입니다")
        return 0


'''
    RPC.update(state=state1, details=details1,
               large_image="tns", large_text="TNS",
               buttons=[{"label": "TNS 봇 초대하기", "url": "https://discord.com/api/oauth2/authorize?client_id=848795383751639080&permissions=8&scope=bot%20applications.commands"},
                        {"label": "TNS 공식 서버", "url": "https://discord.gg/HnBpftKCPu"}]
               )
    while 1:
        time.sleep(600)
'''

win = Tk()
win.title("discord_rpc")
win.geometry('300x600')

label = tkinter.Label(win, text="DISCORD RPC")
label.place(x=5, y=5, width=290, height=30)


label = tkinter.Label(win, text="client_id")
label.place(x=5, y=35, width=290, height=30)

client_id = tkinter.Entry(win)
client_id.place(x=5, y=70, width=290, height=30)

label = tkinter.Label(win, text="details")
label.place(x=5, y=105, width=290, height=30)

details = tkinter.Entry(win)
details.place(x=5, y=140, width=290, height=30)


label = tkinter.Label(win, text="state")
label.place(x=5, y=175, width=290, height=30)

state = tkinter.Entry(win)
state.place(x=5, y=210, width=290, height=30)


label = tkinter.Label(win, text="large_image")
label.place(x=5, y=245, width=290, height=30)

large_image = tkinter.Entry(win)
large_image.place(x=5, y=280, width=290, height=30)


label = tkinter.Label(win, text="small_text")
label.place(x=5, y=315, width=290, height=30)

small_text = tkinter.Entry(win)
small_text.place(x=5, y=360, width=290, height=30)


label = tkinter.Label(win, text="버튼 개수")
label.place(x=5, y=395, width=290, height=30)

list = Listbox(win, height=3)
list.insert(0, "0")
list.insert(1, "1")
list.insert(2, "2")
list.place(x=5, y=430, width=325, height=50)


button = tkinter.Button(win, text="업데이트", command=update)
button.place(x=5, y=495, width=140, height=30)
button = tkinter.Button(win, text="실행하기", command=start)
button.place(x=155, y=495, width=140, height=30)

win.mainloop()
