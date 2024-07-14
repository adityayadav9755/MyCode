import pandas as pd
import numpy as np
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
n = ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas']
s = [12.5, 9.0, 16.5, np.NaN, 9.0, 20.0, 14.5, np.NaN, 8.0, 19.0]
a = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
q = ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes']
dict = {'Name':n, 'Score':s, 'Attempts':a, 'Qualify':q}
df = pd.DataFrame(dict, index=i)
# print(df)
