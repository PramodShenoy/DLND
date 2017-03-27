import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt 

#reading data
dataframe= pd.read_fwf('brain_body.txt')
x_vals=dataframe[['Brain']]
y_vals=dataframe[['Body']]
#training
body_reg=linear_model.LinearRegression()
body_reg.fit(x_vals,y_vals)
#plotting
plt.scatter(x_vals,y_vals)
plt.plot(x_vals,body_reg.predict(x_vals))
plt.show()