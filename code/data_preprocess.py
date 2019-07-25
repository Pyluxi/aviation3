import pandas as pd
from function import str_to_datetime
input_file = '../tmp/cleaned.xls'
output_file = '../tmp/processed.xls'
#读取数据
data = pd.read_excel(input_file)
# 转换格式
data['LOAD_TIME'] = str_to_datetime(data['LOAD_TIME'])
data['FFP_DATE'] = str_to_datetime(data['FFP_DATE'])
data['L'] = data['LOAD_TIME'] - data['FFP_DATE']
#特征提取，只选L,LAST_TO_END,SEG_KM_SUM,avg_discount
#即入会时间离观测结束的天数，最近一次乘机离..的月数，观测窗口的飞行次数,总飞行里程，折扣
data = data[['L','LAST_TO_END','FLIGHT_COUNT','SEG_KM_SUM','avg_discount']]
#重命名属性
data.columns = ['L','R','F','M','C']
#导出
data.to_excel(output_file)




