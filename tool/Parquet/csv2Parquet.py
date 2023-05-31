# csv形式からParquet形式データに変換

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# カラム名を定義 / csv内にカラム名が定期゛されてない場合に利用する
column_names = ['列1', '列2', '列3']

# CSVデータを読み込む
df = pd.read_csv('./filename.csv', encoding="utf-8", names=column_names)

table = pa.Table.from_pandas(df)

# Parquet形式データに変換する
pq.write_table(table, './filename.parquet')