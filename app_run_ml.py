import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
import os
import matplotlib.pyplot as plt


#  查看目錄底下每個檔案的路徑
# for dirname, _, filenames in os.walk(r"C:\Users\mingsan.MINGSAN8611\Desktop\pratice\data"):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

#   matplotlib的中文字體
font = {'family' : 'DFKai-SB',
'weight' : 'bold',
'size'  : '16'}
plt.rc('font', **font) # pass in the font dict as kwargs
plt.rc('axes',unicode_minus=False)

data_train = pd.read_csv(r"C:\Users\mingsan.MINGSAN8611\Desktop\pratice\data\Train.csv")    #windows需要加r

women = data_train.loc[data_train.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)


men = data_train.loc[data_train.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)