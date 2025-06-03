## csv中第二列加入remark列，将有造影的病人数据分出来，标为y，没有的标为n

import pandas as pd
import os

# 假设所有CSV文件都在这个目录下
directory_path = 'newdata_test_1'

# 创建一个新的文件夹来保存更新后的CSV文件
output_directory = 'remark_data'
os.makedirs(output_directory, exist_ok=True)  # 确保输出目录存在

# 读取造影.csv文件，这里假设造影.csv直接包含id列表
angiography_file_path = os.path.join(directory_path, '造影.csv')
try:
    angiography_df = pd.read_csv(angiography_file_path, header=None, encoding='utf-8')
except UnicodeDecodeError:
    angiography_df = pd.read_csv(angiography_file_path, header=None, encoding='gbk')

angiography_ids = angiography_df.iloc[1:, 0].tolist()  # 将ID除去列名转换成列表

# 遍历目录中的所有文件
for file_name in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file_name)
    
    # 确保是CSV文件并且不是造影.csv文件
    if file_name.endswith('.csv') and file_name != '造影.csv':
        print(f'Processing {file_name}...')
        
        # 读取CSV文件
        # df = pd.read_csv(file_path, header=None)
        # 尝试使用UTF-8编码读取，如果失败则使用GBK
        try:
            df = pd.read_csv(file_path, header=None, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, header=None, encoding='gbk')
        
        # 跳过第一行的列名
        # df = df.iloc[1:]
        
        # 添加一个新列，根据是否存在于造影ids列表中来设置值，按列名选取df[0]的列名为0，第一列
        # df['remark'] = df[0].apply(lambda x: 'y' if x[:5] in angiography_ids else 'n')
        # 这里根据每行的第一个元素的前5个字符来判断，df.iloc[:, 0]所有行的第一列
        df['remark'] = df.iloc[1:, 0].apply(lambda x: 'y' if x[:5] in angiography_ids else 'n')
        
        # 将第一行的 "remark" 值填充为 "remark"
        df.loc[0, 'remark'] = 'remark'
        
        # 将新列移到第二列位置
        cols = df.columns.tolist()
        # cols = cols[0:1] + [cols[-1]] + cols[1:-1] # 列名也被匹配了
        cols = cols[0:1] + ['remark'] + cols[1:-1]
        df = df[cols]
        
        # 保存修改后的CSV文件到新目录
        output_file_path = os.path.join(output_directory, file_name)
        df.to_csv(output_file_path, index=False, header=False, encoding='utf-8')  # 假设我们总是输出UTF-8编码的文件
        print(f'{file_name} updated in {output_directory}.')

print('All files have been processed.')
