#匹配UASA狭窄分级和指标
#表2有ID，更新表1对应指标的条目数
#表2没有ID，保持表1原有指标的条目数
#表2有ID，但表1中没有的ID，新增到表1中

import pandas as pd
import numpy as np
from tqdm import tqdm

# 读取文件
table1 = pd.read_csv('data_0620分级/csv/UASA的狭窄最大名单.csv')
table2 = pd.read_csv('data_0620分级/csv/class22.csv')

# 修改table1的ID列
# table2['ID'] = table2['ID'].apply(lambda x: x.split('-')[0])

# 检查并移除重复的ID
table1.drop_duplicates(subset='ID', keep='first', inplace=True)
table2.drop_duplicates(subset='ID', keep='first', inplace=True)

# 查看数据条数
print(f"表1数据条数：{len(table1)}")
print(f"表2数据条数：{len(table2)}")

# 合并数据
merged_table = pd.merge(table1, table2, on='ID', how='left')
# 输出统计结果
print(f"合并后：{len(merged_table)}")

# 删除合并后不需要的列
merged_table = merged_table.drop(columns=['LAD',"LCX","RCA","LM","姓名",'类别',"class22"])

merged_table = merged_table.dropna().reset_index(drop=True)
print(f"删除后：{len(merged_table)}")

# 可选：保存合并后的数据
output_file = 'data_0620分级/csv/class4.csv'
merged_table.to_csv(output_file, index=False)
print(f"合并文件保存在 {output_file}")