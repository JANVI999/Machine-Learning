import pandas as pd
import matplotlib.pyplot as plt

#Mounting the google drive
from google.colab import drive
drive.mount('/content/drive')

#Reading the .csv file and first five elemenets 
data = pd.read_csv('/content/drive/MyDrive/Kaggle/Movies - Sheet1 (1).csv')
data.head()

#x = data.iloc[:,[1,2]].values
#y = data.iloc[:, 3].values
#print(x)
#print(y)

data1 = data[data.RECOMMEND == "y"]
data2 = data[data.RECOMMEND == "n"]

plt.title("OTT platform viwership")
plt.xlabel("Rating")
plt.ylabel("genre")

plt.scatter(data1.RATING, data1.GENRE, color = "blue", label = "Yes", alpha = 0.3)#The alpha blending value, between 0 (transparent) and 1 (opaque)
plt.scatter(data2.RATING, data2.GENRE, color = "green", label = "No", alpha = 0.3)
plt.legend()
plt.show()

# Importing LabelEncoder from Sklearn library from preprocessing Module.
from sklearn.preprocessing import LabelEncoder
 
# Creating a instance of label Encoder.
le = LabelEncoder()
 
# Using .fit_transform function to fit label
# encoder and return encoded label
label = le.fit_transform(data['RATING'])
 
# printing label
label

# removing the column 'RATING' from df as it is of no use now.
data.drop("RATING", axis=1, inplace=True)
 
# Appending the array to our dataFrame  with column name 'RATING'
data["RATING"] = label
 
# printing Dataframe
data

#printing dataframe information after processing it
data.info()

print(data)
# Importing LabelEncoder from Sklearn
# library from preprocessing Module.
from sklearn.preprocessing import LabelEncoder
 
# Creating a instance of label Encoder.
le = LabelEncoder()
 
# Using .fit_transform function to fit label
# encoder and return encoded label
label = le.fit_transform(data['GENRE'])
 
# printing label
label

# removing the column 'GENRE' from df
# as it is of no use now.
data.drop("GENRE", axis=1, inplace=True)
 
# Appending the array to our dataFrame
# with column name 'GENRE'
data["GENRE"] = label
 
# printing Dataframe
data

#printing dataframe information after processing it
data.info()

print(data)
# Importing LabelEncoder from Sklearn
# library from preprocessing Module.
from sklearn.preprocessing import LabelEncoder
 
# Creating a instance of label Encoder.
le = LabelEncoder()
 
# Using .fit_transform function to fit label
# encoder and return encoded label
label = le.fit_transform(data['RECOMMEND'])
 
# printing label
label

# removing the column 'GENRE' from df
# as it is of no use now.
data.drop("RECOMMEND", axis=1, inplace=True)
 
# Appending the array to our dataFrame
# with column name 'GENRE'
data["RECOMMEND"] = label
 
# printing Dataframe
data

#printing dataframe information after processing it
data.info()

data['RATING'] = data['RATING'].astype('float')
data['GENRE'] = data['GENRE'].astype('float')
data['RECOMMEND'] = data['RECOMMEND'].astype('float')
data.info()

x = data.iloc[:,[1,2]].values
y = data.iloc[:, 3].values
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.6, random_state = 42)
#print(x_train)
#print(x_test)
#print(y_train)
#print(y_test)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(x_train, y_train)

model.score(x_test, y_test)

y_pred = model.predict(x_test)

from sklearn.metrics import confusion_matrix
c_mat = confusion_matrix(y_test, y_pred)
print(c_mat)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
