## 此代码在索引相同时候可以跑通，angle文件中同时出现两条数据时会选择第一条数据

import pandas as pd

# 加载第一个CSV文件
df1 = pd.read_csv('data_0403/lad.csv')

# 加载第二个CSV文件
df2 = pd.read_csv('data_0408/齐鲁正常人.csv')

# 将ID列设置为索引
df1.set_index('ID', inplace=True)
df2.set_index('匹配目标ID', inplace=True)

# 删除索引为NaN的数据
df1.dropna(inplace=True)
df2.dropna(inplace=True)

'''
# 删除索引为空的行
df1.dropna(subset=[df1.index.name], inplace=True)
df2.dropna(subset=[df2.index.name], inplace=True)
'''

# 找到重复的索引
duplicates_df1 = df1[df1.index.duplicated()]
duplicates_df2 = df2[df2.index.duplicated()]

# 输出重复的信号格式
if not duplicates_df1.empty:
    print("第一个CSV文件中的重复信号格式：")
    print(duplicates_df1)
else:
    print("第一个CSV文件中没有重复的信号格式。")

if not duplicates_df2.empty:
    print("第二个CSV文件中的重复信号格式：")
    print(duplicates_df2)
else:
    print("第二个CSV文件中没有重复的信号格式。")

# 删除重复的索引
df1 = df1[~df1.index.duplicated()]
df2 = df2[~df2.index.duplicated()]

# 再次找到重复的索引
duplicates_df1 = df1[df1.index.duplicated()]
duplicates_df2 = df2[df2.index.duplicated()]

print("再次检查")
# 输出重复的信号格式
if not duplicates_df1.empty:
    print("第一个CSV文件中的重复信号格式：")
    print(duplicates_df1)
else:
    print("第一个CSV文件中没有重复的信号格式。")

if not duplicates_df2.empty:
    print("第二个CSV文件中的重复信号格式：")
    print(duplicates_df2)
else:
    print("第二个CSV文件中没有重复的信号格式。")

# 将角度数据合并到第一个CSV文件中
df1['心电图判读结果'] = df2['心电图判读结果']
'''
# 输出被加入的数据
added_data = df2.loc[df2.index.difference(df1.index)]
print("被加入的数据：")
print(added_data)
'''
# 保存到新的CSV文件
df1.to_csv('data_0408/合并部分心电判读.csv')
#合并了齐鲁正常人中和lad中没有空值且索引不重复的心电判读数据