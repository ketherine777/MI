import pandas as pd

# 步骤1: 读取主数据CSV文件
main_data = pd.read_csv('data_0513新数据/外部验证/data_0526济宁全部/csv/济宁总.csv',encoding='gbk')  # 请替换为你的主数据文件名

# 步骤2: 读取包含要删除ID的CSV文件
delete_ids = pd.read_csv('data_0513新数据/外部验证/data_0526济宁全部/csv/删除.csv')  # 请替换为你的ID列表文件名，假设只有一列名为'ID'

# 确保ID列的数据类型一致，pandas读取时通常已经是字符串类型，无需额外转换

# 步骤3: 删除指定ID的行
# 使用isin方法检查哪些行的ID在删除列表中，然后用~取反得到需要保留的行
filtered_data = main_data[~main_data['ID'].isin(delete_ids['ID'])]

# 步骤4: 显示或保存过滤后的数据
print(filtered_data)
# 若要保存到新的CSV文件
filtered_data.to_csv('data_0513新数据/外部验证/data_0526济宁全部/csv/济宁总删除后.csv', index=False)  # 替换为你的新文件名