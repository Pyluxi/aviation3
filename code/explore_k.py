import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
input_file = '../tmp/std2.xls'
data = pd.read_excel(input_file)
SSE = []
for k in range(1,9):
    estimator = KMeans(n_clusters=k)
    estimator.fit(data)
    SSE.append(estimator.inertia_)#样本到最近的聚类中心的距离平方之和
X = range(1,9)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X,SSE,'o-')
plt.show()