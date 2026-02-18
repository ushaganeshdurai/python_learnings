import numpy as np
from sklearn.preprocessing import StandardScaler

# Training data
X_train = [[1500, 300000],
           [2000, 450000],
           [2500, 600000],
           [3000, 750000]]


A_train = [[100, 30],
           [200, 4000],
           [50, 600],
           [300, 7500]]

A_test = [[200, 80],
           [80, 70]]




# Test data (new houses)
X_test = [[1800, 400000],
          [2200, 500000]]

scaler = StandardScaler()
# fit() = just calculates and memorizes the mean & std.
#  It doesn't touch your data at all.
# X train will be untouched 

A_train_scaled = scaler.fit_transform(A_train)
A_test_scaled = scaler.transform(A_test)

# The scaler remembers the μ and σ it learned from X_train and
#  uses those same values when you call transform() on X_test


X_train_scaled = scaler.fit(X_train)
# transform() = actually applies the formula z = (x − μ) / σ to convert your raw numbers 
# into scaled numbers.
X_train_transformed = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Never use fit() or fit_transform() on test data. then data leakage will be the prob


print(X_train_scaled) #--.> no data is changed in here
print(X_train_transformed)
print(X_test_scaled)
print(scaler.mean_)     
print(scaler.scale_)