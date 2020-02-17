import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
# import matplotlib
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


font = {'family' : 'DFKai-SB',
'weight' : 'bold',
'size'  : '16'}
plt.rc('font', **font) # pass in the font dict as kwargs
plt.rc('axes',unicode_minus=False)

data_train = pd.read_csv(r"C:\Users\mingsan.MINGSAN8611\Desktop\pratice\data\Train.csv")    #windows需要加r
# print(data_train)
# print(data_train.info())


fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

plt.subplot2grid((2,3),(0,0))             # 在一张大图里分列几个小图
data_train.Survived.value_counts().plot(kind='bar')# 柱状图 
plt.title(u"獲救情況 (1為獲救)") # 标题
plt.ylabel(u"人數")  

plt.subplot2grid((2,3),(0,1))
data_train.Pclass.value_counts().plot(kind="bar")
plt.ylabel(u"人數")
plt.title(u"乘客等級分布")

plt.subplot2grid((2,3),(0,2))
plt.scatter(data_train.Survived, data_train.Age)
plt.ylabel(u"年齡")                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y') 
plt.title(u"按照年齡看獲救分布 (1為獲救)")


plt.subplot2grid((2,3),(1,0), colspan=2)
data_train.Age[data_train.Pclass == 1].plot(kind='kde')   
data_train.Age[data_train.Pclass == 2].plot(kind='kde')
data_train.Age[data_train.Pclass == 3].plot(kind='kde')
plt.xlabel(u"年齡")# plots an axis lable
plt.ylabel(u"密度") 
plt.title(u"各等級的乘客年齡分布")
plt.legend((u'頭等艙', u'2等艙',u'3等艙'),loc='best') # sets our legend for our graph.


plt.subplot2grid((2,3),(1,2))
data_train.Embarked.value_counts().plot(kind='bar')
plt.title(u"各登船口岸上船人數")
plt.ylabel(u"人數")  
plt.show()