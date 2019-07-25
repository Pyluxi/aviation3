import pandas as pd
#读数据
input_file = '../tmp/result2.xls'
output_file = '../tmp/final_result.xls'
data = pd.read_excel(input_file)
#划分客户类别
for i in range(len(data)):
    if data['聚类类别'][i] == 0:
        data['聚类类别'][i] = '低价值客户'

    elif data['聚类类别'][i] == 1:
        data['聚类类别'][i] = '重要保持客户'

    elif data['聚类类别'][i] == 2:
        data['聚类类别'][i] = '重要发展客户'

    elif data['聚类类别'][i] == 3:
        data['聚类类别'][i] = '一般挽留客户'

    else:
        data['聚类类别'][i] = '一般发展客户'

#重命名属性
data.columns = ['L','R','F','M','C','客户类别']
#导出
data.to_excel(output_file,index=None)