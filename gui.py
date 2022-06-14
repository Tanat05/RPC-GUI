from msilib.schema import RadioButton
import tkinter
from tkinter import *
from turtle import update
from pypresence import Presence
import time

from uritemplate import variables


def lister():
    list1 = listb.get()

def update():

    f = open("discord_rpc.txt", 'w')

    client_id1 = client_id.get()
    state1 = state.get()
    details1 = details.get()
    large_image1 =  large_image.get()
    large_text1 =  large_text.get()
    list1 = listb.curselection()
    list1 = str(list1[0])

    f.write(client_id1 + "," + state1 + "," + details1 + "," + large_image1 + "," + large_text1 + "," +list1)
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
win.geometry('300x800')

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


label = tkinter.Label(win, text="large_text")
label.place(x=5, y=315, width=290, height=30)

large_text = tkinter.Entry(win)
large_text.place(x=5, y=360, width=290, height=30)


label = tkinter.Label(win, text="버튼 개수")
label.place(x=5, y=395, width=290, height=30)

listb = Listbox(win, height=0)
listb.insert(0, "0")
listb.insert(1, "1")
listb.insert(2, "2")
listb.place(x=5, y=430, width=325, height=60)

label = tkinter.Label(win, text="button name 1")
label.place(x=5, y=485, width=290, height=30)

button_name1 = tkinter.Entry(win)
button_name1.place(x=5, y=520, width=290, height=30)

label = tkinter.Label(win, text="button url 1")
label.place(x=5, y=555, width=290, height=30)

button_url1 = tkinter.Entry(win)
button_url1.place(x=5, y=590, width=290, height=30)


button = tkinter.Button(win, text="업데이트", command=update)
button.place(x=5, y=655, width=140, height=30)
button = tkinter.Button(win, text="실행하기", command=start)
button.place(x=155, y=655, width=140, height=30)

win.mainloop()

