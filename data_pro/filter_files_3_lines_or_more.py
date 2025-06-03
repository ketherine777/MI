# 筛选文件_移除3行及以上数据

import os
import pandas as pd
import shutil

# 定义文件夹路径
source_folder = 'data/表0531'  # 替换为实际的A文件夹路径
destination_folder = 'data/表0531废弃'  # 替换为实际的目标文件夹路径

# 如果目标文件夹不存在，则创建
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 遍历A文件夹中的每一个CSV文件
for filename in os.listdir(source_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(source_folder, filename)
        
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 判断文件是否有三行以上（包括表头）
        if len(df) > 2:
            # 将文件移到目标文件夹
            shutil.move(file_path, os.path.join(destination_folder, filename))

print("文件处理完成。")
