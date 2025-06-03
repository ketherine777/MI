## 给正常人的数据加上第二列列名为'lad'等的0标签

import pandas as pd

branch = "lcx"

# 读取CSV文件
file_path = f"final_data/{branch}_norm2.csv"  # 替换成您的CSV文件路径
df = pd.read_csv(file_path)

# 添加名为'LAD'的新列，并将其值设为0
df.insert(1, branch.upper(), 0)

# 保存修改后的 DataFrame 到指定路径
output_file_path = f"final_data/{branch}_norm.csv"  # 替换成您想要保存的路径
df.to_csv(output_file_path, index=False)  # 如果不想保存索引，请将 index 参数设置为 False

print(f"{branch} DataFrame 已保存到:", output_file_path)