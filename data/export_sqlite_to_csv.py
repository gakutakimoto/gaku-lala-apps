import sqlite3
import pandas as pd
import os

# データベースのパス
db_file = "/Users/kaisei/Desktop/gaku-lala-apps/data/t3.db3"

# 出力フォルダ
output_folder = "/Users/kaisei/Desktop/gaku-lala-apps/data/csv_output/"

# フォルダがなければ作成
os.makedirs(output_folder, exist_ok=True)

# SQLiteに接続
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# すべてのテーブルを取得
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 各テーブルをCSVにエクスポート
for table in tables:
    table_name = table[0]
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    csv_path = os.path.join(output_folder, f"{table_name}.csv")
    df.to_csv(csv_path, index=False)
    print(f"Exported: {csv_path}")

conn.close()
