import numpy as np
import time

# マトリックスのサイズ
matrix_size = (2000, 2000)

# サンプル行列の生成
matrix = np.random.rand(*matrix_size)

# 計算量が増える複雑な行列の操作を行う関数
def process_matrix_row(row):
    for _ in range(1000):  # 行列の操作を1000回繰り返す
        row = np.sin(row) * np.cos(row)
    return row

# シングルプロセスで行列の操作を実行
def process_matrix_sequential(matrix):
    result = []
    for row in matrix:
        result.append(process_matrix_row(row))
    return np.array(result)

# シングルプロセスでの実行時間を計測
start_time = time.time()
result_sequential = process_matrix_sequential(matrix)
end_time = time.time()
execution_time_sequential = end_time - start_time
print("シングルプロセスの実行時間:", execution_time_sequential, "秒")
