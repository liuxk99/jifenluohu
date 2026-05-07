import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# --- 数据读取部分 ---
# 1. 从 CSV 文件读取数据
# 确保 jifen_data.csv 和这个脚本在同一个文件夹里
df = pd.read_csv("jifen_data.csv")

# 设置绘图风格
plt.figure(figsize=(12, 8.4))
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
# 获取第一条数据（索引0）和最后一条数据（索引-1）的日期
first_date = df.iloc[0]["日期"]      # 第一行
last_date = df.iloc[-1]["日期"]      # 最后一行

plt.title(f"北京市积分落户2026年各区段分值趋势图 ({first_date}-{last_date})", fontsize=14)
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
# plt.show()

# 4. 将图像写入文件
# dpi=300 表示设置分辨率为300，保证图片清晰
# bbox_inches='tight' 确保图例和标签都在图片范围内
plt.savefig("Trends.png", dpi=300, bbox_inches='tight')