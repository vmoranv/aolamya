import os
import re

def find_urls_with_keyword_in_file(file_path, keyword):
    # 正则表达式用于匹配URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\$\$,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        urls = url_pattern.findall(content)
        filtered_urls = [url for url in urls if keyword in url]

        # 获取文件所在的目录和文件名（不带扩展名）
        directory, filename = os.path.split(file_path)
        name_without_ext, ext = os.path.splitext(filename)

        output_file = os.path.join(directory, f'{name_without_ext}_filtered{ext}')
        with open(output_file, 'w', encoding='utf-8') as out_file:
            for url in filtered_urls:
                out_file.write(url + '\n')

        print(f"Found {len(filtered_urls)} URLs containing '{keyword}'. Results saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# 用户输入
file_path = input("Enter the path of the text file to read from: ")
keyword = input("Enter the keyword to filter URLs: ")

# 调用函数
find_urls_with_keyword_in_file(file_path, keyword)
