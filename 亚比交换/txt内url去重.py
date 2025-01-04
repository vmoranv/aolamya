def remove_duplicate_links(file_path):
    # 用于存储唯一链接的集合
    unique_links = set()

    try:
        # 打开并读取用户提供的文件路径中的所有行
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 遍历每一行，并添加到集合中（自动去除重复项）
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:  # 忽略空行
                unique_links.add(stripped_line)

        # 将去重后的链接写入新的文件中
        output_file_path = file_path.rsplit('.', 1)[0] + '_unique.txt'
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for link in sorted(unique_links):  # 可选：对链接进行排序
                output_file.write(link + '\n')

        print(f"Duplicate links have been removed. The result is saved in {output_file_path}.")

    except FileNotFoundError:
        print(f"The file at path {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 用户输入
file_path = input("Enter the path of the text file to read from: ")
remove_duplicate_links(file_path)
