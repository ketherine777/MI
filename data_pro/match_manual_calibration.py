#匹配手动标定指标和标签
#表2有ID，更新表1对应指标的条目数
#表2没有ID，保持表1原有指标的条目数
#表2有ID，但表1中没有的ID，新增到表1中

import pandas as pd
import numpy as np
from tqdm import tqdm

# 读取文件
table1 = pd.read_csv('data_0620分级/csv/class27的无标签表.csv', encoding="GBK")
table2 = pd.read_csv('data_0620分级/csv/所有患者分支信息.csv')
old_branch = 'MAX'
new_branch = 'class32'
#table2 = pd.read_csv('data_0620分级/csv/class4.csv')

# 修改table的ID列
table1['ID'] = table1['ID'].apply(lambda x: x.split('-')[0])
# 删除表21空缺值行
table2 = table2.dropna()
# table2只保留ID和标签列（class22、class4）
table2 = table2[['ID', old_branch]] #"sex", "age",  按照给定顺序保留的

# 检查并移除重复的ID
table1.drop_duplicates(subset='ID', keep='first', inplace=True)
table2.drop_duplicates(subset='ID', keep='first', inplace=True)

# 查看数据条数
print(f"表1数据条数：{len(table1)}")
print(f"表2数据条数：{len(table2)}")

table1 = table1.dropna().reset_index(drop=True)
print(f"1删除空缺后：{len(table1)}")

# 合并数据
merged_table = pd.merge(table1, table2, on='ID', how='left')
# 输出统计结果
print(f"合并后：{len(merged_table)}")

# 重命名class22列
merged_table.rename(columns={old_branch: new_branch}, inplace=True)
# 将最后一列class24列放在第二列
columns = merged_table.columns.tolist()
columns = columns[0:1] + columns[-1:] + columns[1:-1]
merged_table = merged_table[columns]

# 删除合并后不需要的列
# merged_table = merged_table.drop(columns=['LAD',"LCX","RCA","LM","姓名",'类别',"class22"])

merged_table = merged_table.dropna().reset_index(drop=True)
print(f"删除空缺后：{len(merged_table)}")

# 可选：保存合并后的数据
output_file = f'data_0620分级/csv/{new_branch}.csv'
merged_table.to_csv(output_file, index=False)
print(f"合并文件保存在 {output_file}")