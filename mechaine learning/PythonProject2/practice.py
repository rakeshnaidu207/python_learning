import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

dataset=pd.read_csv("Titanic-Dataset.csv")
dataset = dataset[['Survived', 'Pclass', 'Sex', 'Age',
                   'SibSp', 'Parch', 'Fare', 'Embarked']]
print(dataset.head().to_string())
print(dataset.info())
print(dataset.isnull().sum())

numeric_columns=dataset.select_dtypes(include='number').columns
categorical_columns=dataset.select_dtypes(include=['object',"string"]).columns

dataset[numeric_columns]=dataset[numeric_columns].fillna(dataset[numeric_columns].mean())

for column in categorical_columns:
    dataset[column]=dataset[column].fillna(dataset[column].mode()[0])

print(dataset.isnull().sum())

dataset=pd.get_dummies(dataset,columns=categorical_columns,dtype=int,drop_first=True)

print(dataset.info())

correlation=dataset.corr()
sns.heatmap(correlation,annot=True)
plt.show()

x=dataset.drop('Survived',axis=1)
y=dataset["Survived"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
logreg=LogisticRegression(max_iter=1000)
model=DecisionTreeClassifier(random_state=42)
mode1=RandomForestClassifier(n_estimators=100,random_state=42)
svm_model = SVC(kernel='rbf', C=1.0)

logreg.fit(x_train,y_train)
model.fit(x_train,y_train)
mode1.fit(x_train,y_train)
svm_model.fit(x_train,y_train)

y_pred=logreg.predict(x_test)
y_pred1=model.predict(x_test)
y_pred2=mode1.predict(x_test)
y_pred3=svm_model.predict(x_test)

accuracy=accuracy_score(y_test,y_pred)
accuracy1=accuracy_score(y_test,y_pred1)
accuracy2=accuracy_score(y_test,y_pred2)
accuracy3=accuracy_score(y_test,y_pred3)
print(accuracy)
print(accuracy1)
print(accuracy2)
print(accuracy3)

# by comparing all the models logisticregression is getting more accuracy