import pandas as pd 
import numpy as np 

def variable_count(att): 
    types = pd.unique(att) 
    no_of_types = len(types) 
    counts = att.value_counts() 
    return no_of_types, counts, types 

def gini_of_attribute(no_of_types, counts, rows, cla, types, att1, cl): 
    gini_a = 0 
    type_cl_count = 0 
    type_count = 0 
    gini = [] 
    div_index = 0

    if no_of_types == 2: 
        for i in range(len(types)): 
            temp = df.loc[df[att1.name] == types[i]] 
            type_count = len(temp) 
            p = 1 
            for j in range(len(cla)): 
                temp = df.loc[(df[att1.name] == types[i]) & (df[cl.name] == cla[j])] 
                type_cl_count = len(temp) 
                p -= pow((type_cl_count/type_count), 2) 
            gini_a += (type_count/rows) * p 
    elif no_of_types > 2: 
        for i in range(no_of_types): 
            temp1 = df.loc[df[att1.name] == types[i]] 
            temp2 = df.loc[df[att1.name] != types[i]] 
            type_count1 = len(temp1) 
            type_count2 = len(temp2) 
            p1 = 1 
            p2 = 1 
            for j in range(len(cla)): 
                temp3 = df.loc[(df[att1.name] == types[i]) & (df[cl.name] == cla[j])] 
                type_cl_count1 = len(temp3) 
                p1 -= pow((type_cl_count1/type_count1), 2) 
                temp4 = df.loc[(df[att1.name] != types[i]) & (df[cl.name] == cla[j])] 
                type_cl_count2 = len(temp4) 
                p2 -= pow((type_cl_count2/type_count2), 2) 
            gini.append((type_count1/rows) * p1 + (type_count2/rows) * p2) 
        gini_a = min(gini) 
        div_index = gini.index(gini_a) 
    return gini_a, div_index 

df = pd.read_csv('CART.csv') 
col = list(df.columns.values.tolist()) 
cl = df.iloc[:, -1] 
no_of_types, counts, cla = variable_count(cl) 
rows = len(cl) 
gini = 1 - pow((counts[0]/rows), 2) - pow((counts[1]/rows), 2) 
print(gini) 

gini_a = [] 
div = [] 
t = [] 
att = len(df.columns) - 1 

for i in range(att): 
    att1 = df.iloc[:, i] 
    no_of_types, counts, types = variable_count(att1) 
    t.append(types) 
    gini_a1, div_index = gini_of_attribute(no_of_types, counts, rows, cla, types, att1, cl) 
    gini_a.append(gini_a1) 
    div.append(div_index) 

print(gini_a) 
delta_gini = list(map(lambda item: gini - item, gini_a)) 
print(delta_gini) 
index = delta_gini.index(max(delta_gini)) 
print("\n") 
print(col[index], "is the root variable and the variable on one side is ", t[index][div[index]]) 
