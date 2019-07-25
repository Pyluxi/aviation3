import pandas as pd
input_file = '../tmp/processed.xls'
output_file = '../tmp/std2.xls'
data = pd.read_excel(input_file)
data = data[['L','R','F','M','C']]
#重命名属性
# data.columns = ['L','R','F','M','C']
# print(data.head())
# min_max = data.describe().T[['min','max']]
# print(min_max)
#标准化处理
data = (data - data.mean(axis=0))/(data.std(axis=0))
# data = (data - data.mean(axis=0))/(data.std(axis=0))
# print(data.describe().T[['min','max']])
# print(data.head())
data.to_excel(output_file,index=None)