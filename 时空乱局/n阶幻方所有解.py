#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
n阶幻方所有解生成器
使用方法：直接运行脚本，输入幻方阶数即可
"""

def generate_odd_magic_square(n):
    """生成奇数阶幻方的基本解（罗伯法）"""
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        next_i, next_j = (i - 1) % n, (j + 1) % n
        
        if magic_square[next_i][next_j]:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j
    
    return magic_square

def generate_double_even_magic_square(n):
    """生成双偶数阶幻方（4k阶）"""
    magic_square = [[0] * n for _ in range(n)]
    complement = n * n + 1
    
    # 填充初始数字
    for i in range(n):
        for j in range(n):
            magic_square[i][j] = i * n + j + 1
    
    # 交换对角线上的数字
    for i in range(0, n, 4):
        for j in range(0, n, 4):
            for k in range(4):
                # 主对角线
                magic_square[i + k][j + k] = complement - magic_square[i + k][j + k]
                # 副对角线
                magic_square[i + k][j + 3 - k] = complement - magic_square[i + k][j + 3 - k]
    
    return magic_square

def generate_single_even_magic_square(n):
    """生成单偶数阶幻方（4k+2阶）"""
    k = (n - 2) // 4
    size = n // 2
    magic_square = [[0] * n for _ in range(n)]
    
    # 生成四个象限
    quadrant_A = generate_odd_magic_square(size)
    quadrant_D = [[x + size * size for x in row] for row in quadrant_A]
    quadrant_B = [[x + 2 * size * size for x in row] for row in quadrant_A]
    quadrant_C = [[x + 3 * size * size for x in row] for row in quadrant_A]
    
    # 合并四个象限
    for i in range(size):
        for j in range(size):
            magic_square[i][j] = quadrant_A[i][j]
            magic_square[i + size][j + size] = quadrant_B[i][j]
            magic_square[i][j + size] = quadrant_C[i][j]
            magic_square[i + size][j] = quadrant_D[i][j]
    
    # 交换特定位置的元素
    for i in range(size):
        # 交换A和C象限的左侧k列（除中间行）
        if i != size // 2:
            for j in range(k):
                magic_square[i][j], magic_square[i][j + size] = magic_square[i][j + size], magic_square[i][j]
        else:
            for j in range(size // 2 - k + 1, size // 2):
                magic_square[i][j], magic_square[i][j + size] = magic_square[i][j + size], magic_square[i][j]
    
    # 交换B和D象限的中间k-1列
    for i in range(size):
        for j in range(size - k + 1, size):
            magic_square[i + size][j], magic_square[i][j] = magic_square[i][j], magic_square[i + size][j]
    
    return magic_square

def generate_all_symmetries(magic_square):
    """生成给定幻方的所有对称解（旋转和镜像）"""
    symmetries = []
    current = magic_square
    n = len(magic_square)
    
    # 原始解
    symmetries.append([row[:] for row in current])
    
    # 旋转90度、180度、270度
    for _ in range(3):
        current = [[current[n - j - 1][i] for j in range(n)] for i in range(n)]
        symmetries.append([row[:] for row in current])
    
    # 镜像翻转
    mirrored = [row[::-1] for row in magic_square]
    symmetries.append([row[:] for row in mirrored])
    
    # 镜像后的旋转
    current = mirrored
    for _ in range(3):
        current = [[current[n - j - 1][i] for j in range(n)] for i in range(n)]
        symmetries.append([row[:] for row in current])
    
    # 去重
    unique_symmetries = []
    seen = set()
    
    for square in symmetries:
        square_tuple = tuple(tuple(row) for row in square)
        if square_tuple not in seen:
            seen.add(square_tuple)
            unique_symmetries.append([list(row) for row in square])
    
    return unique_symmetries

def is_magic_square(square):
    """验证是否为幻方"""
    n = len(square)
    if n == 0:
        return False
    magic_sum = n * (n * n + 1) // 2
    
    # 检查行和
    for row in square:
        if sum(row) != magic_sum:
            return False
    
    # 检查列和
    for j in range(n):
        if sum(square[i][j] for i in range(n)) != magic_sum:
            return False
    
    # 检查对角线
    diag1 = sum(square[i][i] for i in range(n))
    diag2 = sum(square[i][n - 1 - i] for i in range(n))
    
    return diag1 == magic_sum and diag2 == magic_sum

def print_magic_square(square):
    """打印幻方"""
    n = len(square)
    max_num = n * n
    width = len(str(max_num)) + 1
    
    for row in square:
        print(" ".join(f"{num:{width}}" for num in row))
    print()

def generate_all_magic_squares(n):
    """生成n阶幻方的所有解"""
    if n < 3:
        print("幻方的最小阶数是3")
        return []
    
    if n % 2 == 1:
        print(f"生成奇数阶幻方（{n}阶）")
        base_solution = generate_odd_magic_square(n)
        all_solutions = generate_all_symmetries(base_solution)
    elif n % 4 == 0:
        print(f"生成双偶数阶幻方（{n}阶）")
        base_solution = generate_double_even_magic_square(n)
        all_solutions = generate_all_symmetries(base_solution)
    else:
        print(f"生成单偶数阶幻方（{n}阶）")
        base_solution = generate_single_even_magic_square(n)
        all_solutions = generate_all_symmetries(base_solution)
    
    # 验证所有解
    valid_solutions = []
    for sol in all_solutions:
        if is_magic_square(sol):
            valid_solutions.append(sol)
    
    return valid_solutions

def main():
    print("n阶幻方所有解生成器")
    print("====================")
    
    while True:
        try:
            n = int(input("\n请输入幻方的阶数（n≥3，输入0退出）："))
            if n == 0:
                print("程序结束。")
                break
            if n < 3:
                print("幻方的最小阶数是3，请重新输入。")
                continue
            
            solutions = generate_all_magic_squares(n)
            
            print(f"\n找到 {len(solutions)} 个解：")
            for i, solution in enumerate(solutions, 1):
                print(f"解 {i}:")
                print_magic_square(solution)
                
                # 如果解太多，询问是否继续显示
                if i % 10 == 0 and i < len(solutions):
                    choice = input(f"已显示{i}个解，是否继续显示剩余解？(y/n): ")
                    if choice.lower() != 'y':
                        break
            
            print(f"共找到 {len(solutions)} 个{n}阶幻方解。")
        
        except ValueError:
            print("输入无效，请输入一个整数。")
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
