## 给病人1146数据加angle

import pandas as pd

# 加载第一个CSV文件
df1 = pd.read_csv('data_0330/患者数据只带名字.csv', encoding='GBK')

# 加载第二个CSV文件
df2 = pd.read_csv('data_0330/患者角度.csv', header=None, names=['ID','remark', 'angle']) # encoding='GBK'
# header=None: 这个参数告诉 pandas 不要将文件的第一行视为列名，而是将其作为数据的一部分。因为没有指定列名，所以读取的 DataFrame 不会自动将第一行视为列名。
# names=['ID', 'angle']: 这个参数指定了 DataFrame 的列名。在这里，将第一列命名为 'ID'，第二列命名为 'angle'。由于没有列名行，这个参数是必需的，否则 pandas 将使用默认的列名。
#df2 = pd.read_csv('data_0330/angle.csv', encoding='GBK')

'''
df1['ID'] = df1['ID'].str[:5]
df2['ID'] = df2['ID'].str[:5]

# 对第一个CSV文件中的ID列进行处理，保留前五位作为索引
df1['ID'] = df1['ID'].str.split('-', expand=True)[0]

# 对第二个CSV文件中的ID列进行处理，保留前五位作为索引
df2['ID'] = df2['ID'].str.split('-', expand=True)[0]
'''

# 将ID列设置为索引
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)

print(df1.index.duplicated().any())
print(df2.index.duplicated().any())

duplicate_index = df1.index[df1.index.duplicated()]
print(duplicate_index)
'''
# 删除重复索引，只保留第一条
# df2.drop_duplicates(inplace=True, keep='first')
df2.drop_duplicates(subset='ID', inplace=True, keep='first')
'''
# 检测重复索引
duplicate_index = df2.index[df2.index.duplicated()]
print(duplicate_index)

df1.drop_duplicates(inplace=True)
df2.drop_duplicates(inplace=True)

# 将文件2中angle列的数据添加到文件1中
df1['angle'] = df2['angle']

# 将文件1中文件2中不存在的ID对应的angle设置为空值
df1['angle'].fillna('', inplace=True)

# 保存到新的CSV文件
df1.to_csv('data_0330/测试.csv')
