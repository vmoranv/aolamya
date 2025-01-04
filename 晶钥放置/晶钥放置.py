# 定义原始字符串模板列表
templates = [
    "|#send={\"param\":{\"pms\":\"0\"},\"id\":13,\"cmd\":\"1222\"}|",
    "|#send={\"param\":{\"petId\":0},\"id\":42,\"cmd\":\"ACK241227_4\"}|"
]

# 输出文件的路径
output_file_path = 'replaced_strings.txt'

# 打开文件准备写入
with open(output_file_path, 'w') as file:
    # 遍历数字1到3036
    for num in range(1, 3036):
        # 遍历原始字符串模板
        for template in templates:
            # 替换字符串中的0为当前数字
            new_string = template.replace("0", str(num))
            # 将替换后的字符串写入文件，每个字符串在新的一行上
            file.write(new_string + '\n')

