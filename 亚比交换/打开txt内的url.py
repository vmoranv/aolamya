import webbrowser
import time

def open_links_from_file(file_path):
    try:
        # 打开并读取用户提供的文件路径中的所有行
        with open(file_path, 'r', encoding='utf-8') as file:
            links = [line.strip() for line in file if line.strip()]

        # 依次打开每个链接
        for link in links:
            print(f"Opening {link}")
            webbrowser.open_new_tab(link)

        print("All links have been opened.")

    except FileNotFoundError:
        print(f"The file at path {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 用户输入
file_path = input("Enter the path of the text file containing URLs to open: ")
open_links_from_file(file_path)
