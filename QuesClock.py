from tkinter import *
import time

root = Tk()
root.geometry("600x600")
root.title("TIMER")
ini = 0
timer_r = True
noq = 0
record = ""
t1, t2 = 0, 0


def curtime(t):
    s = int(t % 60)
    m = int((t // 60) % 60)
    h = int(t // 3600)
    return f"{h}:{m}:{s}"


def timer():
    global timer_r
    if timer_r:
        value = curtime(time.time() - ini)
        l1.config(text=value)
        l1.after(1000, timer)
    else:
        return


def start():
    global ini
    ini = time.time()
    timer()


def done():
    global noq, record, t1, t2
    noq += 1
    t1 = t2
    t2 = time.time() - ini
    record = record + f"Q{noq}  {curtime(t2 - t1)}\n"
    l2.config(text=record)


def end():
    global timer_r, noq, t2
    timer_r = False
    text = f"Average time taken per question is {curtime(t2/noq)}"
    l3.config(text=text)


f1 = Frame(root, bg="black")
f1.pack(side="left", fill=Y)
f2 = Frame(root, bg="black")
f2.pack(anchor="nw", fill=Y)

l1 = Label(f1, background="black", foreground="Cyan", font=("Digital-7 Italic", 50))
l1.pack(anchor="center", side=TOP)
l2 = Label(f2, background="black", foreground="Cyan", font=("Digital-7 Italic", 30))
l2.pack(side=LEFT, fill=BOTH)
l3 = Label(f2, background="black", foreground="Cyan", font=("Digital-7 Italic", 50))
l3.pack(anchor="center", side=RIGHT)

b1 = Button(f1, text="Start", command=start, height=8, width=20)
b1.pack(anchor="center", side="top")
b2 = Button(f1, text="Lap", command=done, height=8, width=20)
b2.pack(anchor="center", side="top")
b1 = Button(f1, text="End", command=end, height=8, width=20)
b1.pack(anchor="center", side="top")

root.mainloop()
