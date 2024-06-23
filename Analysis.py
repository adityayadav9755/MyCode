# Importing
import pandas as pd
import pymysql
import sqlalchemy as sa

# Setup and Variables
analysis = sa.create_engine(f"mysql+pymysql://root:Aditya2612@localhost:3306/Analysis")


class Ad:
    df1 = pd.read_sql_query("select TestName, Percentage from Tests where TotalMarks = 96", analysis)
    df2 = pd.read_sql_query("select TestName, Percentage from Tests where TotalMarks = 300", analysis)
    df3 = pd.read_sql_query("select TestName, Percentage from Tests where TotalMarks = 180", analysis)
