# Importing Libraries
from tkinter import *
import mysql.connector
import matplotlib.pyplot as plt

# Setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aditya#@2612",
    database="PROJECT"
)
cursor = db.cursor()
root = Tk()
root.geometry("500x500")
root.title("MY GUI")

#  Variables
u = IntVar()
x = IntVar()
y = IntVar()
z = IntVar()
ugraph = []
xgraph = []
ygraph = []
zgraph = []
n_username = StringVar()
n_password = StringVar()
username = StringVar()
password = StringVar()
cursor.execute("SELECT Username FROM Info")
sql = cursor.fetchone()
for j in sql:
    user = j
cursor.execute("SELECT Password FROM Info")
sql = cursor.fetchone()
for j in sql:
    pas = j

# Functions
def logout():
    db.close()
    frame2.grid_forget()
    frame3.grid_forget()
    menu.delete(1,2)
    username.set("")
    e1.update()
    password.set("")
    e2.update()
    frame1.grid(row=0, column=0, padx=5, pady=5)
def quit():
    root.destroy()
def b1():
    if username.get() == user:
        if password.get() == pas:
            print("Access granted")
            frame2.grid(row=0, column=0, padx=5, pady=5)
            frame1.grid_forget()
            menu.add_cascade(label="File", menu=fm)
            menu.add_cascade(label="Update", menu=um)
            root.update()
        else:
            print("Password is incorrect.")
    else:
        print("Username is incorrect.")
def b2():
    cmd = "INSERT INTO Questions VALUES(%s,%s,%s,%s)"
    val = (u.get(), x.get(), y.get(), z.get())
    cursor.execute(cmd, val)
    db.commit()
    u.set(0)
    x.set(0)
    y.set(0)
    z.set(0)
    e3.update()
    e4.update()
    e5.update()
    e6.update()
def cu():
    frame3.grid(row=4, column=0, padx=5, pady=5)
    e7_l.grid(row=4, column=0, padx=10, pady=10)
    e7.grid(row=4, column=1)
    b3.grid(row=5, column=0, padx=10, pady=10)
def cp():
    frame3.grid(row=4, column=0, padx=5, pady=5)
    e8_l.grid(row=4, column=0, padx=10, pady=10)
    e8.grid(row=4, column=1)
    b4.grid(row=5, column=0, padx=10, pady=10)
def b3():
    val = [n_username.get()]
    cursor.execute("UPDATE Info SET Username=%s", val)
    db.commit()
    frame3.grid_forget()
def b4():
    val = [n_password.get()]
    cursor.execute("UPDATE Info SET Password=%s", val)
    db.commit()
    frame3.grid_forget()
def graph():
    # Getting Data
    i = 0
    cursor.execute("SELECT Day FROM Questions")
    sql = cursor.fetchall()
    for i in sql:
        ugraph.append(i)
    cursor.execute("SELECT Physics FROM Questions")
    sql = cursor.fetchall()
    for i in sql:
        xgraph.append(i)
    cursor.execute("SELECT Chemistry FROM Questions")
    sql = cursor.fetchall()
    for i in sql:
        ygraph.append(i)
    cursor.execute("SELECT Mathematics FROM Questions")
    sql = cursor.fetchall()
    for i in sql:
        zgraph.append(i)
    # Plotting Graph
    plt.plot(ugraph, xgraph, 'o:', label="Physics")
    plt.plot(ugraph, ygraph, 'o:', label="Chemistry")
    plt.plot(ugraph, zgraph, 'o:', label="Mathematics")
    plt.xlabel("Day", fontfamily="Times New Roman", fontsize="15", fontstyle="italic")
    plt.ylabel("No. of Questions", fontfamily="Times New Roman", fontsize="15", fontstyle="italic")
    plt.title("Practice", fontfamily="Algerian", fontsize="20")
    plt.legend()
    plt.show()

def reset():
    sql="DELETE FROM Questions"
    cursor.execute(sql)
    db.commit()
    ugraph = []
    xgraph = []
    ygraph = []
    zgraph = []

# Menubar
menu=Menu(root)

fm=Menu(menu, tearoff=0)
fm.add_command(label="Show Graph", command=graph)
fm.add_command(label="Reset", command=reset)
fm.add_command(label="Logout", command=logout)
fm.add_separator()
fm.add_command(label="Exit", command=quit)

um=Menu(menu, tearoff=0)
um.add_command(label="Change Username", command=cu)
um.add_command(label="Change Password", command=cp)

root.config(menu=menu)

# Frames
frame1=Frame(root, bg="gray", borderwidth=5, relief=RIDGE)
frame1.grid(row=0, column=0, padx=5, pady=5)
frame2=Frame(root,bg="white", borderwidth=5, relief=RIDGE)
frame3=Frame(root,bg="white", borderwidth=5, relief=RIDGE)


# Labels
e1_l=Label(frame1, text="Username:", font="ComicSansMS 10 italic")
e1_l.grid(row=0, column=0, padx=10, pady=10)
e2_l=Label(frame1, text="Password:", font="ComicSansMS 10 italic")
e2_l.grid(row=1, column=0, padx=10, pady=10)
e3_l=Label(frame2, text="Day:", font="ComicSansMS 10 italic")
e3_l.grid(row=0, column=0, padx=10, pady=10)
e4_l=Label(frame2, text="Physics:", font="ComicSansMS 10 italic")
e4_l.grid(row=1, column=0, padx=10, pady=10)
e5_l=Label(frame2, text="Chemistry:", font="ComicSansMS 10 italic")
e5_l.grid(row=2, column=0, padx=10, pady=10)
e6_l=Label(frame2, text="Mathematics:", font="ComicSansMS 10 italic")
e6_l.grid(row=3, column=0, padx=10, pady=10)
e7_l=Label(frame3, text="New Username:", font="ComicSansMS 10 italic")
e8_l=Label(frame3, text="New Password:", font="ComicSansMS 10 italic")

# Entry Widgets
e1=Entry(frame1, textvariable=username)
e1.grid(row=0, column=1)
e2=Entry(frame1, textvariable=password)
e2.grid(row=1, column=1)
e3=Entry(frame2, textvariable=u)
e3.grid(row=0, column=1)
e4=Entry(frame2, textvariable=x)
e4.grid(row=1, column=1)
e5=Entry(frame2, textvariable=y)
e5.grid(row=2, column=1)
e6=Entry(frame2, textvariable=z)
e6.grid(row=3, column=1)
e7=Entry(frame3, textvariable=n_username)
e8=Entry(frame3, textvariable=n_password)

# Button Widgets
b1=Button(frame1, text="LOGIN", command=b1, bg="black", fg="white")
b1.grid(row=3, column=0, padx=10, pady=10)
b2=Button(frame2, text="INSERT", command=b2, bg="black", fg="white")
b2.grid(row=6, column=0, padx=10, pady=10)
b3=Button(frame3, text="CHANGE Username", command=b3, bg="black", fg="white")
b4=Button(frame3, text="CHANGE Password", command=b4, bg="black", fg="white")

root.mainloop()