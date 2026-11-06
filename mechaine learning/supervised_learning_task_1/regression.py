import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# loading of the dataset and data cleaning process
dataset= pd.read_csv("housing.csv")
print(dataset.to_string())
print(dataset.head().to_string())
print(dataset.describe().to_string())
print(dataset.info())
print(dataset.isnull().sum())

# filling the missing values and converting categorical values in to numeric
numeric_column=dataset.select_dtypes(include='number').columns
cater_column=dataset.select_dtypes(include=['object','string']).columns
dataset[numeric_column]=dataset[numeric_column].fillna(dataset[numeric_column].mean())
print(dataset.isnull().sum())
dataset=pd.get_dummies(dataset,columns=cater_column,dtype=int,drop_first=True)
print("_______________________")
print(dataset.to_string())

# for correlation
correlation=dataset.corr()
print(correlation.to_string())

# heat map
plt.figure(figsize=(10,10))
sns.heatmap(correlation,annot=True)
plt.show()

#selecting the x and y
x=dataset.drop('median_house_value',axis=1)
y=dataset["median_house_value"]
#splitting the data for training and testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=7)
# importing the models
regressor=LinearRegression()
regressor1=DecisionTreeRegressor(random_state=42)
regressor2=RandomForestRegressor(n_estimators=10,random_state=42)
regressor3=SVR(kernel="rbf",C=10)

regressor.fit(x_train,y_train)
regressor1.fit(x_train,y_train)
regressor2.fit(x_train,y_train)
regressor3.fit(x_train,y_train)

y_pred=regressor.predict(x_test)
y_pred1=regressor1.predict(x_test)
y_pred2=regressor2.predict(x_test)
y_pred3=regressor3.predict(x_test)

# finding the mean_squared_error
print(mean_squared_error(y_test,y_pred))
print(mean_squared_error(y_test,y_pred1))
print(mean_squared_error(y_test,y_pred2))
print(mean_squared_error(y_test,y_pred3))

#finding the r2_score
print(r2_score(y_test,y_pred))
print(r2_score(y_test,y_pred1))
print(r2_score(y_test,y_pred2))
print(r2_score(y_test,y_pred3))

"note: by observing the results the random forest is predicting well when compare to the remaining models"
"in this code i have used the regression models because the target column in the form decimal formate"
"i have used the  LinearRegression,DecisionTreeRegressor,RandomForestRegressor,SVR models"
"dataset loadeing and data cleaning to covert the columns in to numeric and selected the columns for x and y has done"
"splitting of the data and applying the models and find the r2_score,mean_squared_error"
"and drawn the graph for the model which was predicting good"

#plot for random forest
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred2, alpha=0.5, color='blue', label='Predictions')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2, linestyle='--', label='Perfect Fit')
plt.xlabel('Actual House Value (y_test)')
plt.ylabel('Predicted House Value (y_pred2)')
plt.title('Actual vs. Predicted Median House Values (Random Forest)')
plt.legend()
plt.show()

