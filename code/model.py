import pandas as pd
from sklearn.cluster import KMeans

input_file = '../tmp/std2.xls'
output_file1 = '../tmp/center2.xls'
output_file2 = '../tmp/result2.xls'
#读数据
data = pd.read_excel(input_file)
#聚类类别数
k = 5
#训练模型
model = KMeans(n_clusters=k,n_jobs=4)
model.fit(data)
#聚类中心
kdata = pd.DataFrame(model.cluster_centers_,index=['客户群1','客户群2','客户群3','客户群4','客户群5'],
                     columns=['L','R','F','M','C'])
#聚类类别
data['聚类类别'] = model.labels_
#导出
kdata.to_excel(output_file1)
data.to_excel(output_file2,index=None)
