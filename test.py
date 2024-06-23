import speak
import graph
import database

# say = speak.Speech()
# say.speak(" ")

grph = graph.Graph
df1 = database.Ad.df1
df2 = database.Ad.df2
df3 = database.Ad.df3
# grph.graph(x=[1, 2, 3, 4, 5, 6, 7, 8, 9], y=df1['Percentage'])
# grph.graph(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], y=df2['Percentage'])
# grph.graph(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], y=df3['Percentage'])
grph.graph(y=df1['Percentage'])
grph.graph(y=df2['Percentage'])
grph.graph(y=df3['Percentage'])
grph.show()
