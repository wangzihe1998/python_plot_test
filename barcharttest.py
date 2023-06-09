#仿一张论文插图
#文章：Shifting attention to accuracy can reduce misinformation online (nature)
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
import numpy as np

#准备数据
#横轴标签xLabel
xLabel = ["Extremely\nunlikely", "Moderately\nunlikely", "Slightly\nunlikely", "Slightly\nlikely", "Moderately\nlikely",
          "Extremely\nunlikely"]
#横轴数据controlData，纵轴数据treatmentData
controlData1 = [0.45, 0.16, 0.11, 0.15, 0.1, 0.08]
treatmentData1 = [0.55, 0.17, 0.08, 0.13, 0.07, 0.06]
controlData2 = [0.33, 0.18, 0.16, 0.17, 0.12, 0.08]
treatmentData2 = [0.32, 0.2, 0.14, 0.19, 0.15, 0.06]
controlData3 = [0.46, 0.13, 0.09, 0.135, 0.1, 0.12]
treatmentData3 = [0.53, 0.125, 0.085, 0.125, 0.09, 0.09]
controlData4 = [0.3, 0.19, 0.17, 0.186, 0.12, 0.08]
treatmentData4 = [0.33, 0.17, 0.16, 0.196, 0.128, 0.086]


#画一张柱状图
x=np.arange(6)    #0 1 2 3 4 5
#现在是画第一张图
plt.subplot(2,2,1)
#画图
plt.bar(x,controlData1,width=0.25,label='Control',color="#DB2A1A")
plt.bar(x+0.25,treatmentData1,width=0.25,label='Treatment',color="#5DB0DA")
#添加标题，x标签，y标签
plt.title("Study3\nFalse Headline",family="Times New Roman",size=20)
plt.xlabel("Sharing Likelyhood",family="Times New Roman",size=16)
plt.ylabel("Frequency",family="Times New Roman",size=16)

#去掉上框线和右框线
ax=plt.gca()  #gca:get current axis得到当前轴
#设置图片的右边框和上边框为不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#设置x轴的刻度标签
plt.xticks(x,xLabel,family='Times New Roman')
plt.yticks(np.arange(0,0.7,0.1),family='Times New Roman')

# 显示图例

# 定义图例的字体
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 15,
        }
plt.legend(prop=font, frameon=False)

######################################################################################
# 现在是画第二张图
plt.subplot(2, 2, 2)

# 画图
plt.bar(x, controlData2, width=0.25, label='Cotrol', color="#5DB0DA")
plt.bar(x + 0.25, treatmentData2, width=0.25, label='Treatment', color="#DB2A1A")

# 添加标题，x标签，y标签
plt.title("Study3\nTrue Headline", family="Times New Roman", size=20)
plt.xlabel("Sharing Likelyhood", family="Times New Roman", size=16)
plt.ylabel("Frequency", family="Times New Roman", size=16)

# 去掉上框线和右框线
ax = plt.gca()  # gca:get current axis得到当前轴
# 设置图片的右边框和上边框为不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x轴的刻度标签
plt.xticks(x, xLabel, family='Times New Roman')
plt.yticks(np.arange(0, 0.7, 0.1), family='Times New Roman')

# 显示图例

# 定义图例的字体
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 15,
        }
plt.legend(prop=font, frameon=False)


###################################################################################
# 现在是画第三张图
plt.subplot(2, 2, 3)

# 画图
plt.bar(x, controlData3, width=0.25, label='Cotrol', color="#5DB0DA")
plt.bar(x + 0.25, treatmentData3, width=0.25, label='Treatment', color="#DB2A1A")

# 添加标题，x标签，y标签
plt.title("Study4\nFalse Headline", family="Times New Roman", size=20)
plt.xlabel("Sharing Likelyhood", family="Times New Roman", size=16)
plt.ylabel("Frequency", family="Times New Roman", size=16)

# 去掉上框线和右框线
ax = plt.gca()  # gca:get current axis得到当前轴
# 设置图片的右边框和上边框为不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x轴的刻度标签
plt.xticks(x, xLabel, family='Times New Roman')
plt.yticks(np.arange(0, 0.7, 0.1), family='Times New Roman')

# 显示图例

# 定义图例的字体
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 15,
        }
plt.legend(prop=font, frameon=False)


##################################################################################
# 现在是画第四张图
plt.subplot(2, 2, 4)

# 画图
plt.bar(x, controlData4, width=0.25, label='Cotrol', color="#5DB0DA")
plt.bar(x + 0.25, treatmentData4, width=0.25, label='Treatment', color="#DB2A1A")

# 添加标题，x标签，y标签
plt.title("Study4\nTrue Headline", family="Times New Roman", size=20)
plt.xlabel("Sharing Likelyhood", family="Times New Roman", size=16)
plt.ylabel("Frequency", family="Times New Roman", size=16)

# 去掉上框线和右框线
ax = plt.gca()  # gca:get current axis得到当前轴
# 设置图片的右边框和上边框为不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x轴的刻度标签
plt.xticks(x, xLabel, family='Times New Roman')
plt.yticks(np.arange(0, 0.7, 0.1), family='Times New Roman')

# 显示图例

# 定义图例的字体
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 15,
        }
plt.legend(prop=font, frameon=False)

plt.subplots_adjust(wspace=0.12, hspace=0.53)


plt.show()