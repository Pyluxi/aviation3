import pandas as pd

# data = pd.read_excel('../tmp/cleaned.xls')
# cleaned = data.describe(percentiles=[],include='all').T
# #统计空值数
# cleaned['null'] = len(data) - cleaned['count']
# cleaned = cleaned[['null','max','min']]
# cleaned.columns = ['空值数','最大值','最小值']
data = pd.read_excel('../tmp/result2.xls')
# print(data.head())
# print(data.columns[-1])
# for i in range(len
data.columns = ['L','R','F','M','C','客户类别']
print(data.columns)
# print(list(data.columns))
# list(data.columns)[-1] = '客户类别'
# print(data.columns)
# (data)):
#     if data['SUM_YR_1'][i] & data['SUM_YR_2'][i]:
#         print(data[i])

# print(data.describe())
# attributes = data.describe().T
#
# print(attributes['count'])

# data = pd.read_excel("../tmp/explore.xls",index_col='属性')
# print(cleaned.loc[['SUM_YR_1','SUM_YR_2','avg_discount','SEG_KM_SUM']])
# print(data.head())

# help(data.loc)