base_code = '|#send={"cmd":"54_22","id":15,"param":{"ft":0,"type":99,"floor":118,"handler":"MB240607",":ext_seq;":2096970}}||#time=15000'
output_lines = []

for floor in range(166, 201):
    new_code = base_code.replace('"floor":118', f'"floor":{floor}')
    output_lines.append(new_code)

# 将行写入文本文件
with open('output.txt', 'w') as file:
    for line in output_lines:
        file.write(line + '\n')
