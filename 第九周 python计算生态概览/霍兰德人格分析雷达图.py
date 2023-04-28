# -- coding: utf-8 --
import numpy as np
import matplotlib.pyplot as plt
# 如果需要使用中文标签，还需添加以下代码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为中文黑体
# 数据
data = [[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
        [0.85, 0.75, 0.30, 0.25, 0.20, 0.40],
        [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
        [0.20, 0.30, 0.85, 0.45, 0.32, 0.25],
        [0.19, 0.22, 0.40, 0.90, 0.92, 0.28],
        [0.62, 0.55, 0.27, 0.25, 0.35, 0.30]]

# 角度（弧度）
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)

# 重复第一个角度以使图像闭合
angles = np.concatenate((angles, [angles[0]]))

# 职业
occupations = ['工程师', '实验员', '艺术家', '推销员', '记事员', '社会工作者', '技术员']

# 绘图
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
for i in range(len(data)):
    # 绘制折线图
    ax.plot(angles, data[i]+data[i][:1], 'o-', linewidth=2, label=occupations[i])
    # 填充颜色
    ax.fill(angles, data[i]+data[i][:1], alpha=0.25)
# 添加坐标轴标签
ax.set_thetagrids(angles*180/np.pi, occupations)
# 添加标题
plt.title('Holland Personality Analysis', fontsize=20)
# 添加图例
plt.legend(loc='best')
# 显示图形
plt.show()
