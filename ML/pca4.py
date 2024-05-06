import pandas as pd
import numpy as np
from numpy.linalg import eig

df = pd.read_csv('Salary_Data.csv')
x = df.iloc[:, 0]
y = df.iloc[:, 1]

mew1 = round((sum(x) / len(x)), 2)
mew2 = round((sum(y) / len(y)), 2)

mean = [mew1, mew2]
print(mean)

x_new = list(map(lambda x1: round((x1 - mew1), 2), x))
y_new = list(map(lambda y1: round((y1 - mew2), 2), y))

cov = np.array([[0, 0], [0, 0]])
for i in range(0, len(x_new)):
    temp = np.array([[float(x_new[i])], [float(y_new[i])]])
    temp1 = temp.transpose()
    temp2 = temp @ temp1
    cov = cov + temp2

cov = cov / len(x_new)

eigenvalues, eigenvectors = eig(cov)

feat = eigenvectors[:, 1]

new_values = []
for i in range(0, len(x_new)):
    temp = np.array([[float(x_new[i])], [float(y_new[i])]])
    temp1 = feat @ temp
    new_values.append(temp1.tolist())

print(new_values)
