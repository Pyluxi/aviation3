import pandas as pd
from function import count_category
import matplotlib.pyplot as plt

input_file = '../tmp/result.xls'
output_file = '../tmp/count.xls'
data = pd.read_excel(input_file)
#计算各个类别的数量
count = count_category(data['聚类类别'])

# print(count)
# print(sum(count) == len(data))

count_d = pd.Series(count,index=['客户群体1','客户群体2','客户群体3','客户群体4','客户群体5'])

# count_d.to_excel(output_file)


