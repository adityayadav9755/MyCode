from tkinter import *

root= Tk()
root.geometry("500x500")
root.title("MY GUI")

def b1():
    f=open("Graphics2_1.txt", "a")
    f.write(username.get()+"\n")


mb= Frame(root, bg="gray10", borderwidth=6)
mb.pack(side=TOP, fill=X)

mb_l1=Menubutton(mb, text="Menu", font="Times 10 bold", fg="white", bg="gray10", relief="flat")
mb_l1.pack(side=LEFT, padx=10)

mb_l2=Menubutton(mb, text="File", font="Times 10 bold", fg="white", bg="gray10", relief="flat")
mb_l2.pack(side=LEFT, padx=10)

mb_l3=Menubutton(mb, text="Edit", font="Times 10 bold", fg="white", bg="gray10", relief="flat")
mb_l3.pack(side=LEFT, padx=10)

sb= Frame(root, bg="gray20", borderwidth=6)
sb.pack(side=LEFT, fill=Y)
sb_l1= Label(sb, text="Project Details", font="Times 15 bold", fg="white", bg="black", relief="sunken", width="20")
sb_l1.pack()

username= StringVar()

e_l1=Label(root, text="Username:")
e_l1.pack(anchor="nw", side=LEFT, pady=100)

e1=Entry(root, textvariable=username)
e1.pack(anchor="nw", side=LEFT, pady=100)

b1=Button(root, text="SUBMIT", command=b1)
b1.pack()


Ad= Label(sb, text='''Hi, Aditya. This is your first GUI. \nCongratulations on this achievement.
This software is going to be \nhelpful for you in your studies. \nYou can use this to track your progress
''', font="Times 10 bold", fg="white", bg="black", relief="sunken", width="40")
Ad.pack()

root.mainloop()