import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
labels = '低价值客户','重要保持客户','重要发展客户','一般挽留客户','一般发展客户'
sizes = [24659,5536,4184,15740,12125]
colors = ['yellowgreen','gold','lightskyblue','lightcoral','red']
explode = [0,0.1,0.1,0,0] #突出显示高价值客户

plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        autopct='%1.1f%%',shadow=True,startangle=90)

plt.axis('equal')
plt.show()