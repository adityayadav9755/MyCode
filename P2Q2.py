import pandas as pd

i = [0, 1, 2, 3]
c = ["alpha-romero", "alpha-romero", "alpha-romero", "audi"]
b = ["convertible", "convertible", "hatchback", "sedan"]
w = [88.6, 88.6, 94.5, 99.8]
l = [168.8, 168.8, 171.2, 176.6]
e = ["dohc", "dohc", "ohcv", "ohc"]
n = ["four", "four", "six", "four"]
h = [111, 111, 154, 102]
a = [21, 21, 19, 24]
p = [13495.0, 16500.0, 16500.0, 13950.0]

df = pd.DataFrame({"Index":i, "Company":c, "Body-style":b,\
                    "Wheel-base":w, "Length":l, "Engine-type":e,\
                    "Num-of-cylinders":n, "Horsepower":h, "Average-mileage":a,\
                    "Price":p})
