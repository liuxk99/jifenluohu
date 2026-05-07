import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# 构建数据
data = {
    "日期": ["4/22", "4/23", "4/24", "4/25", "*4/26", "*4/27", "4/28", "4/29", "4/30", "5/1", "*5/2", "*5/3", "*5/4", "*5/5", "*5/6", "5/7"],
    "1-1000": [122.67, 122.84, 122.96, 123.01, 123.04, 123.05, 123.12, 123.16, 123.17, 123.21, 123.21, 123.21, 123.21, 123.21, 123.22, 123.25],
    "1001-2000": [121.21, 121.42, 121.67, 121.75, 121.79, 121.80, 121.92, 121.97, 122.04, 122.08, 122.09, 122.09, 122.09, 122.09, 122.09, 122.13],
    "2001-3000": [120.34, 120.63, 120.80, 120.88, 120.92, 120.92, 121, 121.05, 121.09, 121.13, 121.17, 121.17, 121.17, 121.17, 121.17, 121.21],
    "3001-4000": [119.38, 119.84, 120.09, 120.17, 120.25, 120.29, 120.38, 120.46, 120.54, 120.58, 120.59, 120.59, 120.63, 120.63, 120.63, 120.67],
    "4001-5000": [118.29, 118.88, 119.26, 119.46, 119.51, 119.58, 119.75, 119.88, 119.97, 120.01, 120.04, 120.05, 120.05, 120.05, 120.05, 120.13],
    "5001-6000": [117.13, 117.92, 118.46, 118.67, 118.75, 118.84, 119.05, 119.25, 119.38, 119.46, 119.47, 119.50, 119.50, 119.50, 119.51, 119.59]
}

df = pd.DataFrame(data)

# 设置绘图风格
plt.figure(figsize=(12, 7))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False

# 绘制曲线
columns = ["1-1000", "1001-2000", "2001-3000", "3001-4000", "4001-5000", "5001-6000"]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

for col, color in zip(columns, colors):
    plt.plot(df["日期"], df[col], marker='o', label=col, color=color, linewidth=2)

# 1. 获取当前的坐标轴对象
ax = plt.gca()

# 2. 设置 Y 轴主刻度的间隔为 0.1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# 3. (可选) 如果图表太拥挤，可以只显示次要刻度线而不显示标签
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

# 添加标题和标签
plt.title("各区段分值变换趋势图 (4/22-5/7)", fontsize=14)
plt.xlabel("日期", fontsize=12)
plt.ylabel("分值", fontsize=12)

plt.grid(True, axis='both') # 同时显示横向和纵向参考线
# plt.grid(True, linestyle='--', alpha=0.6)
# 3. 确保网格线同时显示主刻度和次要刻度
ax.grid(which='major', axis='y', linestyle='-', linewidth='0.8', color='grey') # 主网格
ax.grid(which='minor', axis='y', linestyle='--', linewidth='0.5', color='lightgrey') # 次网格

plt.legend(title="数据区段", bbox_to_anchor=(1.05, 1), loc='upper left')

# 自动调整布局
plt.tight_layout()
plt.show()