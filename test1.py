import pandas as pd
import os
# import numpy as np
# dict1 = {'India': 'NewDelhi', 'UK': 'London', 'Japan': 'Tokyo'}
# ar1 = np.array([2, 9, 8, 26, 12, 6])
# ar2 = np.array([1, 2, 3, 4, 5, 6])
# s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# s2 = pd.Series(ar1, index=['a', 'b', 'c', 'd', 'e', 'f'])
# s3 = pd.Series(dict1)
# s3.name = 'Capitals'
# s3.index.name = 'Country'
# s3['France'] = 'Paris'
dict2 = {'Maths': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
         'Science': pd.Series([4, 5, 6], index=['a', 'b', 'c']),
         'English': pd.Series([7, 8, 9], index=['a', 'b', 'c'])}
d1 = pd.DataFrame(dict2)
d1.loc['d'] = [10, 11, 12]
d1.to_excel("C:\\Users\\Dell\\Desktop\\Folders\\CSV.xlsx")
os.startfile("C:\\Users\\Dell\\Desktop\\Folders\\CSV.xlsx")
d1.to_sql()
