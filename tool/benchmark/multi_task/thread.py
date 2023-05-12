import numpy as np
import concurrent.futures
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

# マルチスレッドで行列の操作を並列化する
def process_matrix_parallel(matrix):
    result = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_matrix_row, row) for row in matrix]
        for future in concurrent.futures.as_completed(futures):
            result.append(future.result())
    return np.array(result)

# マルチスレッドでの実行時間を計測
start_time = time.time()
result_parallel = process_matrix_parallel(matrix)
end_time = time.time()
execution_time_parallel = end_time - start_time
print("マルチスレッドの実行時間:", execution_time_parallel, "秒")

