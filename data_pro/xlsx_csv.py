import os
import pandas as pd

# 设置数据集的根目录和子文件夹路径
base_folder_path = 'data_250429论文三'
xlsx_folder_path = os.path.join(base_folder_path, 'xlsx')
csv_folder_path = os.path.join(base_folder_path, 'csv')

# 如果csv文件夹不存在，则创建
if not os.path.exists(csv_folder_path):
    os.makedirs(csv_folder_path)

# 获取xlsx文件夹中的所有xlsx文件
for file_name in os.listdir(xlsx_folder_path):
    if file_name.endswith('.xlsx'):
        # 读取xlsx文件
        file_path = os.path.join(xlsx_folder_path, file_name)
        
        # 遍历xlsx文件中的每个sheet
        for sheet_name in pd.ExcelFile(file_path, engine='openpyxl').sheet_names:
            # 读取sheet数据
            df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
            
            # 删除整列都是缺失值的列
            df = df.dropna(axis=1, how='all')
            # 删除整行都是缺失值的行
            df = df.dropna(axis=0, how='all')
            
            # 检查是否为空表
            if not df.empty:
                # 生成csv文件名，按照原xlsx文件名和sheet名命名
                # csv_file_name = f"{os.path.splitext(file_name)[0]}_{sheet_name}.csv"
                # 按照原xlsx文件名命名
                csv_file_name = f"{os.path.splitext(file_name)[0]}.csv"
                # 按照sheet命名
                # csv_file_name = f"{sheet_name}.csv"
                csv_file_path = os.path.join(csv_folder_path, csv_file_name)
                
                # 将数据保存为csv文件，并且不写入索引
                df.to_csv(csv_file_path, index=False)
                
                # 输出保存信息
                print(f"{csv_file_name} 已保存在 {csv_folder_path}")
            else:
                # 输出空表信息
                print(f"{file_name} 的 {sheet_name} 是空表，未生成csv文件。")

print("所有xlsx文件已转换为csv文件。")