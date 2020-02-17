import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
import os
import matplotlib.pyplot as plt


#  check doc in folder path
# for dirname, _, filenames in os.walk(r"C:\Users\mingsan.MINGSAN8611\Desktop\pratice\data"):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

#   matplotlib chinese front
font = {'family' : 'DFKai-SB',
'weight' : 'bold',
'size'  : '16'}
plt.rc('font', **font) # pass in the font dict as kwargs
plt.rc('axes',unicode_minus=False)

data_train = pd.read_csv(r"C:\Users\mingsan.MINGSAN8611\Desktop\pratice\data\Train.csv")    #windows need add "r"
data_test = pd.read_csv(r"C:\Users\mingsan.MINGSAN8611\Desktop\pratice\data\test.csv")
# women = data_train.loc[data_train.Sex == 'female']["Survived"]
# rate_women = sum(women)/len(women)

# print("% of women who survived:", rate_women)


# men = data_train.loc[data_train.Sex == 'male']["Survived"]
# rate_men = sum(men)/len(men)

# print("% of men who survived:", rate_men)





#   then think about first machine learning model

from sklearn.ensemble import RandomForestClassifier
y = data_train["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(data_train[features])
X_test = pd.get_dummies(data_train[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': data_test.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)
print("Your submission was successfully saved!")