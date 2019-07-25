import pandas as pd
from sklearn.cluster import KMeans
from function import rader_chart
import matplotlib.pyplot as plt

#获取数据
input_file = '../tmp/std2.xls'
output_png = '../tmp/analysis.png'
data = pd.read_excel(input_file)
#拟合模型
k = 5
kmodel = KMeans(n_clusters=k,n_jobs=4)
kmodel.fit(data)

r1 = pd.DataFrame(kmodel.cluster_centers_)
r2 = pd.Series(kmodel.labels_).value_counts()
print(r1)
print("===================")

#
max = r1.values.max()
min = r1.values.min()
r = pd.concat([r1,r2],axis=1) #横向连接
# # print(r)
r.columns = list(data.columns) + ['类别数目']

#绘图
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111,polar=True)
center_num = r.values
feature = ['入会时间','飞行时间间隔','飞行次数','总飞行里程','平均折扣率']
# N = len(feature)
#枚举
plt = rader_chart(center_num,feature,min,max)
plt.savefig(output_png)
plt.show()