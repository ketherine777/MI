#匹配磁补偿后的数据和标签与原表剩余指标
#表2有ID，更新表1对应指标的条目数
#表2没有ID，保持表1原有指标的条目数
#表2有ID，但表1中没有的ID，新增到表1中

import pandas as pd
import numpy as np
from tqdm import tqdm

# 读取文件
table1 = pd.read_csv('data_0620分级/csv/class21.csv')
table2 = pd.read_csv('data_0620分级/csv/磁补偿后疾病分类.csv')

# 修改table1的ID列
table2['ID'] = table2['ID'].apply(lambda x: x.split('-')[0])

# 检查并移除重复的ID
table1.drop_duplicates(subset='ID', keep='first', inplace=True)
table2.drop_duplicates(subset='ID', keep='first', inplace=True)

# 查看数据条数
print(f"表1数据条数：{len(table1)}")
print(f"表2数据条数：{len(table2)}")

# 合并数据
merged_table = pd.merge(table1, table2, on='ID', how='left', suffixes=('_table1', '_table2'))

# 更新指标
for column in tqdm(table1.columns, desc="Updating columns"):
    if column in table2.columns and column != 'ID': #确保只对那些同时存在于 table1 和 table2 中的非 ID 列进行更新操作
        # 创建一个映射字典，如果 ID 存在于 table2 中，则更新为 table2 的值，否则保持原始值
        update_dict = dict(zip(table2['ID'], table2[column]))
        table1[column] = table1.apply(lambda row: update_dict.get(row['ID'], row[column]), axis=1)

# 找到仅在 table2 中存在的 ID 并添加到 table1 中
new_rows = table2[~table2['ID'].isin(table1['ID'])]
table1 = pd.concat([table1, new_rows], ignore_index=True, join='outer')

# 统计数据条数
count_table1_with_id_from_table2 = table1[table1['ID'].isin(table2['ID'])].shape[0]
count_table1_without_id_from_table2 = table1[~table1['ID'].isin(table2['ID'])].shape[0]
count_table2_ids_not_in_table1 = new_rows.shape[0]

# 输出统计结果
print(f"表2有ID，更新表1对应指标的条目数：{count_table1_with_id_from_table2}")
print(f"表2没有ID，保持表1原有指标的条目数：{count_table1_without_id_from_table2}")
print(f"表1没有表2的ID，新增ID及对应指标的条目数：{count_table2_ids_not_in_table1}")

# 可选：保存合并后的数据
table1.to_csv('data_0620分级/csv/class22.csv', index=False)
