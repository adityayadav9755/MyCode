import pandas as pd
import numpy as np

idx = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
s = ["Anastasia", "Dima", "Katherine", "James", "Emily", "Michael", "Matthew", "Laura", "Kevin", "Jonas"]
m = [72.5, 90.0, 66.5, np.NaN, 29, 28, 74.5, np.NaN, 80, 19]
sem = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
res = ["Pass", "Fail", "Pass", "Fail", "Fail", "Pass", "Pass", "Fail", "Fail", "Pass"]

df = pd.DataFrame({"Stname":s, "Marks":m, "Semester":sem, "Result":res}, index=idx)

