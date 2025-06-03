## 原csv数据中每行为一通道数据，将数据展平，合并为同一个csv，加入新的列名

import os
import pandas as pd

# 存储所有CSV文件的文件夹路径
folder_path = '/RAID5/projects/fuxingwen/wjq/myocardial_ischemia/data_0526双盲表/表'

# 用于存储所有数据的DataFrame
merged_data = pd.DataFrame()

# 循环读取文件夹中的每个CSV文件
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        
        # 读取CSV文件
        data = pd.read_csv(file_path, delimiter=",")
        
        # 获取'channel'列的值
        channel_col = data['channel']

        # 去掉'channel'列
        data.drop(columns=['channel'], inplace=True)
        
        original_columns = data.columns

        # 重塑数据以每个通道编号的指标值排列在一起
        reshaped_data = data.stack().to_frame().T

        # 生成新的列名,由于嵌套循环导致16*9*16=2304个列报错
        new_columns = [f"{channel}_{col}" for channel in channel_col for col in data.columns]
        reshaped_data.columns = new_columns

        # 添加ID列
        file_name_without_extension = os.path.splitext(filename)[0]
        id_value = file_name_without_extension.split('_')[-1] #分支表里是ID-姓名
        reshaped_data.insert(0, 'ID', id_value)
        #reshaped_data.insert(0, 'ID', file_name_without_extension) #总表是只有ID
        
        # 将数据添加到合并数据中
        merged_data = pd.concat([merged_data, reshaped_data], axis=0, ignore_index=True)

# 保存合并后的数据为CSV文件
output_file_path = '/RAID5/projects/fuxingwen/wjq/myocardial_ischemia/data_0526双盲表/表.csv'
merged_data.to_csv(output_file_path, index=False)
print(f"合并后的数据已保存到文件: {output_file_path}")