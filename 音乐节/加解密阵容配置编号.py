import json
import base64
import os

def decrypt_base64_to_json(content):
    """将Base64内容解密为JSON格式"""
    try:
        # 解码Base64
        decoded_bytes = base64.b64decode(content)
        decoded_str = decoded_bytes.decode('utf-8')
        
        # 将字符串解析为JSON对象
        json_data = json.loads(decoded_str)
        
        # 返回格式化后的JSON字符串
        return json.dumps(json_data, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"解密错误: {str(e)}"

def encrypt_json_to_base64(content):
    """将JSON内容加密为Base64格式"""
    try:
        # 尝试加载JSON
        json_data = json.loads(content)
        
        # 转换为紧凑JSON格式
        compact_json = json.dumps(json_data, separators=(',', ':'), ensure_ascii=False)
        
        # 编码为Base64
        encoded_bytes = base64.b64encode(compact_json.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"加密错误: {str(e)}"

def detect_file_content(content):
    """检测文件内容类型"""
    # 尝试解析为JSON
    try:
        json.loads(content)
        return 'json'
    except:
        pass
    
    # 检查是否是有效的Base64
    try:
        base64.b64decode(content)
        return 'base64'
    except:
        pass
    
    return 'unknown'

def main():
    print("=" * 50)
    print("Base64编解码工具")
    print("=" * 50)
    
    # 选择操作模式
    print("\n请选择操作模式:")
    print("1. 解密 (Base64 → JSON)")
    print("2. 加密 (JSON → Base64)")
    mode = input("请输入选项(1/2): ").strip()
    
    if mode not in ['1', '2']:
        print("无效的选项!")
        return
    
    input_path = input("\n请输入文件路径: ").strip()
    
    if not os.path.exists(input_path):
        print("文件不存在!")
        return
    
    # 读取文件内容
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    # 检测文件类型
    file_type = detect_file_content(content)
    
    # 确定输出路径和扩展名
    script_dir = os.path.dirname(__file__)
    if mode == '1':  # 解密
        output_path = os.path.join(script_dir, 'output.json')
    else:  # 加密
        output_path = os.path.join(script_dir, 'output.txt')
    
    if mode == '1':  # 解密
        print("\n正在进行Base64解密...")
        if file_type == 'base64':
            result = decrypt_base64_to_json(content)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"解密完成! JSON结果已保存到: {output_path}")
        else:
            print("错误：文件内容不是有效的Base64格式")
    
    elif mode == '2':  # 加密
        print("\n正在进行JSON加密...")
        if file_type == 'json':
            result = encrypt_json_to_base64(content)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"加密完成! Base64结果已保存到: {output_path}")
        else:
            print("错误：文件内容不是有效的JSON格式")

if __name__ == "__main__":
    main()
