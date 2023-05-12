import numpy as np
from multiprocessing import Pool
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

# マルチプロセスで行列の操作を並列化する
def process_matrix_parallel(matrix):
    pool = Pool()  # プロセスプールの作成
    result = pool.map(process_matrix_row, matrix)  # マルチプロセスで行列の操作を並列実行
    pool.close()
    pool.join()
    return np.array(result)

# マルチプロセスでの実行時間を計測
start_time = time.time()
result_parallel = process_matrix_parallel(matrix)
end_time = time.time()
execution_time_parallel = end_time - start_time
print("マルチプロセスの実行時間:", execution_time_parallel, "秒")
