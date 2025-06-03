import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(10000))  # 读取文件的前 10000 字节进行编码检测
    return result['encoding']


def process_and_save_dataset(file_name):
    # 检测文件编码
    file_encoding = detect_encoding(file_name)

    # 加载数据集
    data = pd.read_csv(file_name,encoding=file_encoding)

    # 选择需要填充的列（这里假设所有列都需要填充）
    # columns_to_fill = data.columns
    # 填充检测出的数值，忽略字符串
    numeric_columns_to_fill = data.select_dtypes(include=['float64', 'int64']).columns

    # 初始化IterativeImputer
    imputer = IterativeImputer(max_iter=10, random_state=42)

    # 使用IterativeImputer填充空缺值
    # data_filled = imputer.fit_transform(data[columns_to_fill])
    data[numeric_columns_to_fill] = imputer.fit_transform(data[numeric_columns_to_fill])

    # 将填充后的数据转换为DataFrame
    #data_filled_df = pd.DataFrame(data_filled, columns=columns_to_fill)

    # 将填充后的数据和原数据的非空缺值列合并
    #data_processed = pd.concat([data[data.columns.difference(columns_to_fill)], data_filled_df], axis=1)

    # 保存处理后的数据集为原文件名_processed.csv
    processed_file_name = file_name.replace('.csv', '_processed.csv')
    data.to_csv(processed_file_name, index=False)

    print(f"Processed dataset saved as {processed_file_name}")

# 批量处理三个数据集
dataset_files = ['data/LADdata.csv', 'data/LCXdata.csv', 'data/RCAdata.csv']

for dataset_file in dataset_files:
    process_and_save_dataset(dataset_file)