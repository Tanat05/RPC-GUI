from msilib.schema import RadioButton
import tkinter
from tkinter import *
from turtle import update
from pypresence import Presence
import os
import sys
import subprocess
import pyautogui


def on_closing():
    res = pyautogui.confirm("정말 프로그램을 종료하시겠습니까?")
    if res is not None and str(res) == "OK":
        sys.exit(1)
    else:
        pass


def update():
    client_id1 = client_id.get()
    state1 = state.get()
    details1 = details.get()
    large_image1 = large_image.get()
    large_text1 = large_text.get()
    list1 = listb.curselection()
    button_name11 = button_name1.get()
    button_url11 = button_url1.get()
    button_name22 = button_name2.get()
    button_url22 = button_url2.get()

    if client_id1 == "" or state1 == "" or details1 == "":
        tkinter.messagebox.showwarning("오류", "빈칸이 있습니다")
        return
    try:
        list1 = str(list1[0])
    except:
        tkinter.messagebox.showwarning("오류", "버튼의 개수를 선택해주세요")
        return 0

    if list1 == "1":
        if button_name11 == "" or button_url11 == "":
            tkinter.messagebox.showwarning(
                "오류", "버튼 개수 1을 선택하였습니다\n버튼1 제목,URL을 입력하셔야 합니다")
            return
    if list1 == "2":
        if button_name11 == "" or button_url11 == "" or button_name22 == "" or button_url22 == "":
            tkinter.messagebox.showwarning(
                "오류", "버튼 개수 2을 선택하였습니다\n버튼1 제목,URL 와 버튼2 제목,URL을 입력하셔야 합니다")
            return

    f = open("discord_rpc.txt", 'w')
    f.write(client_id1 + "," + state1 + "," + details1 + "," +
            large_image1 + "," + large_text1 + "," + list1 + "," + button_name11 + "," + button_url11 + "," + button_name22 + "," + button_url22)
    f.close()

    win = Tk()
    win.title("discord_rpc")
    win.geometry('300x200')

    label = tkinter.Label(win, text="업데이트가 완료되었습니다")
    label.place(x=5, y=80, width=290, height=30)
    win.mainloop()


def stop():
    win.destroy()
    subprocess.call(["python", os.path.join(
        sys.path[0], __file__)] + sys.argv[1:])


def start():
    try:
        f = open("discord_rpc.txt", 'r')
        line = f.readline()
        line = line.split(",")
        try:
            RPC = Presence(client_id=line[0])
            RPC.connect()
        except:
            tkinter.messagebox.showwarning("오류", "잘못된 client_id입니다")
            sys.exit()

        try:
            if line[5] == "1":
                RPC.update(state=line[1], details=line[2], large_image=line[3],
                           large_text=line[4], buttons=[{"label": line[6], "url": line[7]}])

            if line[5] == "2":
                RPC.update(state=line[1], details=line[2],
                           large_image=line[3], large_text=line[4],
                           buttons=[{"label": line[6], "url": line[7]},
                                    {"label": line[8], "url": line[9]}]
                           )
            else:
                RPC.update(details=line[1], state=line[2])
        except Exception as e:
            tkinter.messagebox.showwarning("오류", "실행이 실패하였습니다\n" + str(e))
        f.close()
    except Exception as e:
        tkinter.messagebox.showwarning(
            "오류", "discord_rpc.txt 파일을 찾을 수 없습니다\n처음 한번 업데이트를 해주세요\n또한 discord_rpc.txt파일을 이 프로그램 파일과 같은 경로에 두세요")
        sys.exit()
    win.title("실행 중")
    button = tkinter.Button(win, text="중단하기", command=stop)
    button.place(x=5, y=650, width=590, height=30)

    win.mainloop()


win = Tk()
win.title("discord_rpc")
win.geometry('600x690')

label = tkinter.Label(win, text="DISCORD RPC", font=("", 30))
label.place(x=155, y=20, width=290, height=30)


label = tkinter.Label(win, text="client_id")
label.place(x=5, y=90, width=290, height=30)

client_id = tkinter.Entry(win)
client_id.place(x=5, y=120, width=290, height=30)

label = tkinter.Label(win, text="내용 1")
label.place(x=5, y=170, width=290, height=30)

details = tkinter.Entry(win)
details.place(x=5, y=200, width=290, height=30)


label = tkinter.Label(win, text="내용 2")
label.place(x=300, y=170, width=290, height=30)

state = tkinter.Entry(win)
state.place(x=300, y=200, width=290, height=30)


label = tkinter.Label(win, text="이미지 이름")
label.place(x=5, y=250, width=290, height=30)

large_image = tkinter.Entry(win)
large_image.place(x=5, y=280, width=290, height=30)


label = tkinter.Label(win, text="이미지 내용")
label.place(x=300, y=250, width=290, height=30)

large_text = tkinter.Entry(win)
large_text.place(x=300, y=280, width=290, height=30)


label = tkinter.Label(win, text="버튼 개수")
label.place(x=5, y=360, width=290, height=30)

listb = Listbox(win, height=0)
listb.insert(0, "0")
listb.insert(1, "1")
listb.insert(2, "2")
listb.place(x=5, y=390, width=290, height=55)

label = tkinter.Label(win, text="버튼1 제목")
label.place(x=5, y=460, width=290, height=30)

button_name1 = tkinter.Entry(win)
button_name1.place(x=5, y=490, width=290, height=30)

label = tkinter.Label(win, text="버튼1 URL")
label.place(x=300, y=460, width=290, height=30)

button_url1 = tkinter.Entry(win)
button_url1.place(x=300, y=490, width=290, height=30)

label = tkinter.Label(win, text="버튼2 제목")
label.place(x=5, y=540, width=290, height=30)

button_name2 = tkinter.Entry(win)
button_name2.place(x=5, y=570, width=290, height=30)

label = tkinter.Label(win, text="버튼2 URL")
label.place(x=300, y=540, width=290, height=30)

button_url2 = tkinter.Entry(win)
button_url2.place(x=300, y=570, width=290, height=30)


button = tkinter.Button(win, text="업데이트", command=update)
button.place(x=5, y=650, width=290, height=30)
button = tkinter.Button(win, text="실행하기", command=start)
button.place(x=305, y=650, width=290, height=30)

win.protocol("WM_DELETE_WINDOW", on_closing)

win.mainloop()
