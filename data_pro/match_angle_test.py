## 此代码在索引相同时候可以跑通，angle文件中同时出现两条数据时会选择第一条数据

import pandas as pd

# 加载第一个CSV文件
df1 = pd.read_csv('data_0401/processed_norm_data.csv')

# 加载第二个CSV文件
df2 = pd.read_csv('data_0401/processed_angle_data.csv')

# 将ID列设置为索引
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)

# 将角度数据合并到第一个CSV文件中
df1['angle'] = df2['angle']

# 保存到新的CSV文件
df1.to_csv('data_0401/测试.csv')
