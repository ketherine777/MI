# 将csv中文表头改成对应的英文
import csv

# 读取转置文件，构建英文到中文表头的映射字典
header_mapping = {}
with open('data_0417需要转置的表/CSV_METADATA8274799674384082278_transposed前两行.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    en_headers = next(reader)
    cn_headers = next(reader)
    header_mapping = dict(zip(en_headers, cn_headers))

# 打印前五个对应关系
print("前五个对应关系：")
for en_header, cn_header in list(header_mapping.items())[:5]:
    print(f"{en_header} -> {cn_header}")

# 读取原始CSV文件，将英文表头替换为中文表头
output_rows = []
with open('data_0417需要转置的表/英文版本.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        output_row = [header_mapping.get(header, header) for header in row]
        output_rows.append(output_row)

# 写入新的CSV文件
with open('data_0417需要转置的表/中文版本.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

print("转换完成！")
