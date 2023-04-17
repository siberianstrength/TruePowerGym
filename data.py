import pandas as pd
import random as r
data = pd.read_csv("vehicles.csv")
df = pd.DataFrame(data)
def get_random_data_one_byte(n):
    array = []
    for i in range(n):
        array.append(r.randint(0,9))
    return array
def get_data(n,dt):
    if dt != "posting_date":
        array = []
        temp = df.loc[0:n-1,[dt]]
        temparray = temp.values
        for i in range(len(temparray)):
            array.append(temparray[i][0])
        return array
    else:
        array = []
        temp = df.loc[27:n+26,[dt]]
        temparray = temp.values
        for i in range(len(temparray)):
            array.append(temparray[i][0])
        return array
def copy(array):
    return[array[i] for i in range(len(array))]