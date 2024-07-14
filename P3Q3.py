import P3Q2

df = P3Q2.df

# r,c = 0,0
# for i,j in df.isna().iterrows():
#     for k in j:
#         if k is True:
#             r += 1
#             break
# for i,j in df.isna().items():
#     for k in j:
#         if k is True:
#             c += 1
#             break
# print(f"Number of rows in DataFrame with NaN value are {r}.\nNumber of columns in DataFrame with NaN value are {c}.")

# df.loc[108, "Marks"] = 71.5

#df["Subjects"] = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']

# for i,j in df.iterrows():
#     if j["Result"] == "Fail":
#         print(j)

#print(len(df.columns))

#df.rename(columns={"Marks":"ObtMarks"}, inplace=True)
