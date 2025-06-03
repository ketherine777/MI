## 每个csv为一行，合并csv

import pandas as pd
import os

def merge_csv_files(directory, output_file):
    # 创建一个空的DataFrame来存储所有的数据
    all_data = pd.DataFrame()

    # 遍历指定目录下的所有csv文件
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # 读取csv文件
            df = pd.read_csv(os.path.join(directory, filename))

            # 去掉文件名的扩展名
            filename_without_extension = os.path.splitext(filename)[0]
            
            '''
            # 使用破折号拆分文件名
            num, name = filename_without_extension.split('-')

            # 将文件名添加到新的两列
            df.insert(0, 'num', num)
            df.insert(1, 'name', name)
            '''
            
            df.insert(0, 'ID', filename_without_extension)
            
            # 将数据添加到all_data DataFrame
            all_data = pd.concat([all_data, df])

    # 删除整列都是空数据的列
    all_data = all_data.dropna(axis=1, how='all')

    # 将合并后的数据写入新的csv文件
    all_data.to_csv(output_file, index=False)

# 调用函数
merge_csv_files('data06预处理/0615轻症和亚健康/小于50新旧指标/新旧指标', 'data06预处理/0615轻症和亚健康/小于50新旧指标/小于50表.csv')
