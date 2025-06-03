# 分支匹配新指标数据和旧标签

import pandas as pd

# 读取表1（ID标签）和表2（ID指标）的数据
table1 = pd.read_csv('data06预处理/0611新指标数据集/csv/匹配患者.csv')
table2 = pd.read_csv('data06预处理/0611新指标数据集/csv/患者表.csv')
output_dir = 'data06预处理/0611新指标数据集/csv/'
person = '患者'

# 定义要处理的分支
branches = ['LAD', 'LCX', 'RCA', 'LM']

# 患者有010-，不能用此逻辑
# 处理表1的ID，使其只包含前面的部分
table1['Original_ID1'] = table1['ID']
table1['ID'] = table1['ID'].apply(lambda x: x.split('-')[0])

# 处理表2的ID，使其只包含前面的部分
table2['Original_ID2'] = table2['ID']
table2['ID'] = table2['ID'].apply(lambda x: x.split('-')[0])

for branch in branches:
    # 筛选表1中当前分支标签为0.0的人物
    # normal_people = table1[table1[branch] == 0.0]
    
    # 从表2中找到对应的ID和其指标, 设置合并方式为'inner',只保留匹配到的数据; 设置合并方式为'left',保留左表（表1）的所有数据
    merged_data = pd.merge(table1, table2, on='ID', how='left')
    
    # 保留所需的列
    # final_data = merged_data[['ID', branch] + list(table2.columns[1:])]
    
    # 确定要使用的原始ID列名
    merged_data['Final_ID'] = merged_data['Original_ID2'].combine_first(merged_data['Original_ID1'])

    # 保留所需的列，并加回原始ID，去table2的最后一列（'Original_ID2'）列
    final_data = merged_data[['Final_ID', branch] + list(table2.columns[1:-1])].copy()

    # 将原始ID列重命名为ID
    final_data.rename(columns={'Final_ID': 'ID'}, inplace=True)
    
    # 生成相应的CSV文件
    final_data.to_csv(f'{output_dir}/{branch}_{person}.csv', index=False)

    print(f'{branch}{person}匹配完成')
