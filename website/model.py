# import the necessary modules
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# load the csv files
df = pd.read_csv('iris.csv')

# print(df.head())
# print(df.tail())
# print(df.iloc[110:140])
X = df.drop('species', axis=1)
y = df['species']
# # print(X)
# #print(y)

# split dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)

# feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# instantiate the model
rfc = RandomForestClassifier()

# fit the model
rfc.fit(X_train, y_train)

# make the pickle file for model
pickle.dump(rfc, open('iris_rfc.pkl', 'wb'))	#search what wb means

