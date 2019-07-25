import pandas as pd
#读取数据
input_file = '../data/air_data.csv'
output_file = '../tmp/explore.xls'
data = pd.read_csv(input_file,encoding='utf-8')
explore = data.describe(percentiles=[],include='all').T
#统计空值数
explore['null'] = len(data) - explore['count']
explore = explore[['null','max','min']]
explore.columns = ['空值数','最大值','最小值']
#导出
explore.to_excel(output_file)
# print(len(data))
# print(explore['count'])
# print(len(data) - explore['count'])
# print(explore)
# print(data.head())
# print(data.describe())
