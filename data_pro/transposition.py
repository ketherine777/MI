# 将data_0417需要转置的表/CSV_METADATA8274799674384082278.xls读出，转存为csv，转置后，再存为csv文件

import pandas as pd

# 读取数据表，不标记缺失值，全视为字符串
# data = pd.read_excel('data_0417需要转置的表/CSV_METADATA8274799674384082278.xls', keep_default_na=False)
# 读取数据表的前两列
data = pd.read_excel('data_0417需要转置的表/CSV_METADATA8274799674384082278.xls', usecols=range(2), keep_default_na=False)

# 将数据转换为字符串，并替换百分号为另一个字符（比如空格）
data_str = data.astype(str)
data_str.replace('\n', ' ', regex=True, inplace=True)  # 替换换行符为空格
# data_str.replace('%', ' ', regex=True, inplace=True)  # 替换百分号为空格

# 保存转置后的数据为csv文件
data_str.T.to_csv('data_0417需要转置的表/CSV_METADATA8274799674384082278_transposed前两行.csv', sep=',', index=False, header=False, encoding='utf-8')

# 输出已经完成……
print("已经完成转置并保存为CSV文件。")

