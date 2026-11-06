import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, MeanShift
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split

# loading the data set and data cleaning.
dataset=pd.read_csv("Mall_Customers.csv")

print(dataset.head().to_string())
print(dataset.info())
print(dataset.describe())

"""the dataset dont have any null values so no need of data cleaning """

catogorical_columns=dataset.select_dtypes(include=["string","object"]).columns
# converted string in to integers for better understand to the model
dataset=pd.get_dummies(dataset,columns=catogorical_columns,dtype=int,drop_first=True)

print(dataset.info())

#correlation
correlation=dataset.corr()

sns.heatmap(correlation,annot=True)
plt.title("Correlation Matrix")
plt.show()

#selecting of x and applying the feature selection and modeling
x=dataset.drop("CustomerID",axis=1)
x_train,x_unseen=train_test_split(x,test_size=0.2,random_state=42)

scaler=StandardScaler()
x_scaler=scaler.fit_transform(x_train)
x_unseen=scaler.transform(x_unseen)

model=KMeans(n_clusters=2,random_state=10,n_init=10).fit(x_scaler)
model1=DBSCAN(eps=1.0,min_samples=5).fit(x_scaler)
model2=MeanShift(bandwidth=2,n_jobs=-1).fit(x_scaler)

y_pred=model.labels_
y_pred1=model1.labels_
y_pred2=model2.labels_

u_pred=model.predict(x_unseen)
u_pred2=model2.predict(x_unseen)
knn=KNeighborsClassifier(n_neighbors=1).fit(x_scaler,y_pred1)
u_pred1=knn.predict(x_unseen)

print("kmeans:", silhouette_score(x_scaler, y_pred))
print("mean_shift:", silhouette_score(x_scaler, y_pred2))

if len(set(y_pred1)) > 1:
    print("dbscan:", silhouette_score(x_scaler, y_pred1))

for title, seen_lbl in [("k_mean", y_pred), ("DBSCAN", y_pred1), ("mean_shift", y_pred2)]:
    plt.title(title)
    sns.scatterplot(x=x_scaler[:, 0], y=x_scaler[:, 1], hue=seen_lbl, legend="full", s=60)
    plt.scatter(x_unseen[:, 0], x_unseen[:, 1], c="red", marker="*",
                s=200, edgecolors="black", label="unseen")
    plt.xlabel("Age (scaled)")
    plt.ylabel("Annual Income (scaled)")
    plt.legend()
    plt.show()

print("kmeans unseen:", pd.Series(u_pred).value_counts().to_dict())
print("dbscan unseen:", pd.Series(u_pred1).value_counts().to_dict())
print("mean_shift unseen:", pd.Series(u_pred2).value_counts().to_dict())

