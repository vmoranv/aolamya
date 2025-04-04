#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

/**
 * @brief 判断当前幻方是否符合规则
 * @param grid 幻方矩阵
 * @return 是否合法幻方
 */
bool isMagicSquare(const vector<vector<int>>& grid) {
    int n = grid.size();
    if (n == 0) return false;

    int target_sum = n * (n * n + 1) / 2;

    // 检查行和
    for (int i = 0; i < n; ++i) {
        int row_sum = 0;
        for (int j = 0; j < n; ++j) {
            row_sum += grid[i][j];
        }
        if (row_sum != target_sum) return false;
    }

    // 检查列和
    for (int j = 0; j < n; ++j) {
        int col_sum = 0;
        for (int i = 0; i < n; ++i) {
            col_sum += grid[i][j];
        }
        if (col_sum != target_sum) return false;
    }

    // 检查主对角线
    int diag1 = 0;
    for (int i = 0; i < n; ++i) {
        diag1 += grid[i][i];
    }
    if (diag1 != target_sum) return false;

    // 检查副对角线
    int diag2 = 0;
    for (int i = 0; i < n; ++i) {
        diag2 += grid[i][n - 1 - i];
    }
    if (diag2 != target_sum) return false;

    return true;
}

/**
 * @brief 生成奇数阶幻方的所有解
 * @param n 幻方阶数
 * @param solutions 存储所有解的容器
 */
void generateOddMagicSquares(int n, vector<vector<vector<int>>>& solutions) {
    vector<pair<int, int>> positions(n * n);
    vector<vector<int>> grid(n, vector<int>(n, 0));

    int i = 0;
    int j = n / 2;

    for (int num = 1; num <= n * n; ++num) {
        grid[i][j] = num;
        positions[num - 1] = { i, j };

        int next_i = (i - 1 + n) % n;
        int next_j = (j + 1) % n;

        if (grid[next_i][next_j] != 0) {
            i = (i + 1) % n;
        }
        else {
            i = next_i;
            j = next_j;
        }
    }

    solutions.push_back(grid);

    // 生成旋转和反射变换的幻方
    for (int k = 1; k < 4; ++k) {
        vector<vector<int>> rotated(n, vector<int>(n, 0));
        for (int x = 0; x < n; ++x) {
            for (int y = 0; y < n; ++y) {
                rotated[y][n - 1 - x] = grid[x][y];
            }
        }
        solutions.push_back(rotated);
        grid = rotated;
    }

    vector<vector<int>> reflected(n, vector<int>(n, 0));
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < n; ++y) {
            reflected[x][n - 1 - y] = grid[x][y];
        }
    }
    solutions.push_back(reflected);

    grid = reflected;
    for (int k = 1; k < 4; ++k) {
        vector<vector<int>> rotated(n, vector<int>(n, 0));
        for (int x = 0; x < n; ++x) {
            for (int y = 0; y < n; ++y) {
                rotated[y][n - 1 - x] = grid[x][y];
            }
        }
        solutions.push_back(rotated);
        grid = rotated;
    }
}

/**
 * @brief 生成双偶数阶幻方（4k阶）的所有解
 * @param n 幻方阶数
 * @param solutions 存储所有解的容器
 */
void generateDoublyEvenMagicSquares(int n, vector<vector<vector<int>>>& solutions) {
    vector<vector<int>> grid(n, vector<int>(n, 0));

    // 填充数字1到n²
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            grid[i][j] = i * n + j + 1;
        }
    }

    // 标记需要交换的格子
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            // 检查是否在中心小方块或角上小方块
            bool condition1 = (i % 4 == 0 || i % 4 == 3) && (j % 4 == 0 || j % 4 == 3);
            bool condition2 = (i % 4 == 1 || i % 4 == 2) && (j % 4 == 1 || j % 4 == 2);

            if (condition1 || condition2) {
                grid[i][j] = n * n + 1 - grid[i][j];
            }
        }
    }

    solutions.push_back(grid);

    // 生成旋转和反射变换的幻方
    for (int k = 1; k < 4; ++k) {
        vector<vector<int>> rotated(n, vector<int>(n, 0));
        for (int x = 0; x < n; ++x) {
            for (int y = 0; y < n; ++y) {
                rotated[y][n - 1 - x] = grid[x][y];
            }
        }
        solutions.push_back(rotated);
        grid = rotated;
    }
}

/**
 * @brief 生成单偶数阶幻方（4k+2阶）的所有解
 * @param n 幻方阶数
 * @param solutions 存储所有解的容器
 */
void generateSinglyEvenMagicSquares(int n, vector<vector<vector<int>>>& solutions) {
    int m = n / 2;
    vector<vector<vector<int>>> sub_solutions;
    generateOddMagicSquares(m, sub_solutions);

    for (auto& A : sub_solutions) {
        vector<vector<int>> grid(n, vector<int>(n, 0));

        // 填充四个象限
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < m; ++j) {
                // A象限 (左上)
                grid[i][j] = A[i][j];
                // B象限 (右上)
                grid[i][j + m] = A[i][j] + 2 * m * m;
                // C象限 (左下)
                grid[i + m][j] = A[i][j] + 3 * m * m;
                // D象限 (右下)
                grid[i + m][j + m] = A[i][j] + m * m;
            }
        }

        int k = (n - 2) / 4;

        // 交换A和C象限的特定格子
        for (int i = 0; i < m; ++i) {
            int start_j = (i == m / 2) ? m / 2 : 0;
            for (int j = start_j; j < start_j + k; ++j) {
                if (j < m) {
                    swap(grid[i][j], grid[i + m][j]);
                }
            }
        }

        // 交换B和D象限的特定格子
        for (int i = 0; i < m; ++i) {
            for (int j = m + m / 2 - k + 1; j < m + m / 2; ++j) {
                if (j < n) {
                    swap(grid[i][j], grid[i + m][j]);
                }
            }
        }

        solutions.push_back(grid);
    }
}

/**
 * @brief 打印幻方
 * @param grid 幻方矩阵
 */
void printMagicSquare(const vector<vector<int>>& grid) {
    int n = grid.size();
    int width = to_string(n * n).length() + 1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << setw(width) << grid[i][j];
        }
        cout << endl;
    }
    cout << endl;
}

int main() {
    int n;
    cout << "请输入幻方的阶数n: ";
    cin >> n;

    if (n < 3) {
        cout << "幻方的阶数必须大于等于3" << endl;
        return 1;
    }

    vector<vector<vector<int>>> solutions;

    if (n % 2 == 1) {
        // 奇数阶幻方
        generateOddMagicSquares(n, solutions);
    }
    else if (n % 4 == 0) {
        // 双偶数阶幻方
        generateDoublyEvenMagicSquares(n, solutions);
    }
    else {
        // 单偶数阶幻方
        generateSinglyEvenMagicSquares(n, solutions);
    }

    cout << "共找到 " << solutions.size() << " 个解:" << endl;
    for (size_t i = 0; i < solutions.size(); ++i) {
        cout << "解 " << i + 1 << ":" << endl;
        printMagicSquare(solutions[i]);

        // 验证幻方是否正确
        if (!isMagicSquare(solutions[i])) {
            cout << "警告: 此解不符合幻方规则!" << endl;
        }
    }

    return 0;
}
