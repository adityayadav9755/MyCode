import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine("mysql+pymysql://root:Aditya2612@localhost:3306/School")


def menu():
    choice = int(input('''\nList of operations that you can perform:
1.Insert data into a table.
2.Read data from a table.
Enter your choice: '''))
    if choice == 1:
        insert()
    elif choice == 2:
        read()
    else:
        print("You did not enter a valid choice.\n")


def insert():
    try:
        table = input("Enter table name: ")
        fieldlist = list(pd.read_sql("select * from " + table, engine).columns)
        values = {}
        for x in fieldlist:
            data = input("Enter " + x + ": ")
            values[x] = data
        df = pd.DataFrame(values, index=[0])
        df.to_sql(table, engine, if_exists="append", index=False)

    except ValueError:
        print("You did not enter valid data.\n")


def update():
    pass


def read():
    table = input("Enter table name: ")
    df = pd.read_sql("select * from " + table, engine)
    print(df)


uname = input("Enter the username: ")
try:
    pwd1 = pd.read_sql_query(f"select pwd from employee where uname =" + "\'" + uname + "\'", engine).iloc[0, 0]
    pwd = input("Enter the password: ")
    if pwd == pwd1:
        while True:
            menu()
    else:
        print("You entered the wrong password!")

except ValueError or IndexError:
    print("Username is incorrect!")
