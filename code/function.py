#将string转换为datetime
def str_to_datetime(data):
    from datetime import datetime
    for i in range(len(data)):
        data[i] = datetime.strptime(data[i],'%Y/%m/%d')
    return data


# data["LOAD_TIME"] = pd.to_datetime(data["LOAD_TIME"])
# data["FFP_DATE"] = pd.to_datetime(data["FFP_DATE"])
# data["入会时间"] = data["LOAD_TIME"] - data["FFP_DATE"]

# r1 = pd.Series(kmodel.labels_).value_counts()
#统计类别数
def count_category(category,k=5):
    #列表初始化
    count = [0 for n in range(k)]
    for i in range(len(category)):
        for j in range(k):
            if category[i] == j: #统计每个类别数
                count[j] = count[j] + 1
    # for i in range(k):
    #     t = 0
    #     for j in range(len(category)):
    #         if category[j] == i:  #统计每个类别数
    #             count[i] = ++t
    return count

def rader_chart(center_num,feature,min,max):
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, polar=True)
    N = len(feature)
    for i, v in enumerate(center_num):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # print(i,v)
        # 设置雷达图的角度,用于平分切开一个圆面
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
        # 封闭雷达图一圈
        center = np.concatenate((v[:-1], [v[0]]))  # 串联
        angles = np.concatenate((angles, [angles[0]]))
        # 绘制折线图
        ax.plot(angles, center, 'o-', linewidth=2, label="第%d类人群,%d人" % (i + 1, v[-1]))
        # 填充颜色
        ax.fill(angles, center, alpha=0.25)
        # 添加每个特征标签
        ax.set_thetagrids(angles * 180 / np.pi, feature, fontsize=15)
        ax.set_ylim(min - 0.1, max + 0.1)
        plt.title('客户群特征分析图', fontsize=20)
        # 添加网格线
        ax.grid(True)
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), ncol=1, fancybox=True, shadow=True)
    return plt