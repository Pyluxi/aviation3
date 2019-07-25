import pandas as pd
#读取数据
input_file = '../data/air_data.csv'
output_file = '../tmp/cleaned.xls'
data = pd.read_csv(input_file,encoding='utf-8')
#过滤掉票价为空的数据
data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
#过滤掉票价为0，折扣不为0，总里程大于0的数据
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['avg_discount'] == 0 ) & (data['SEG_KM_SUM'] == 0)
data = data[index1 | index2 | index3]
#导出
data.to_excel(output_file)
