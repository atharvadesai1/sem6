import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
import random

hours_study = [29, 15, 33, 28, 39, 20, 10, 35, 25, 32,
               30, 18, 27, 38, 22, 12, 37, 24, 34, 31,
               26, 21, 14, 36, 17, 23, 16, 11, 40, 19,
               41, 44, 47, 50, 46, 43, 49, 45, 48, 42,
               51, 54, 57, 60, 56, 53, 59, 55, 58, 52]

pass_fail = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1,
             1, 0, 1, 1, 0, 0, 1, 0, 1, 1,
             1, 0, 0, 1, 0, 1, 0, 0, 1, 0,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Load data
df = pd.DataFrame({'Hours of Study': hours_study, 'Pass/Fail': pass_fail})

# Normalize features
df['Hours of Study'] = (df['Hours of Study'] - df['Hours of Study'].mean()) / df['Hours of Study'].std()

# Extract features and target
X = df.iloc[:, 0].values
y = df.iloc[:, 1].values

X = X.reshape(-1, 1)
print(X.shape)
print(y.shape)

# Initialize weights randomly
w = np.random.randn(X.shape[1])
print(f'w: {w}')

# Hyperparameters
alpha = 0.01
epochs = 100

# Training loop
for epoch in range(epochs):
    z = np.dot(X, w)
    y_pred = 1 / (1 + np.exp(-z))
    gradient = np.dot(X.T, (y - y_pred))
    w += alpha * gradient

# Predictions
y_pred = np.where(y_pred > 0.5, 1, 0)
print(f'Y Pred: {y_pred}')
print(f'Y Actual: {list(np.array(y))}')

y_actual = list(np.array(y))
# Calculating accuracy/
numerator = 0
denominator = len(y_actual)

for i in range(len(y_pred)):
    if y_pred[i] == y_actual[i]:
        numerator += 1

accuracy = (numerator / denominator)*100
print(f'Accuracy of Logistic Regression: {accuracy}%')

