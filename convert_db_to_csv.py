import sqlite3
import pandas as pd
import os

# データベースファイルのパス
db_path = "/Users/kaisei/Desktop/gaku-lala-apps/data/new_t3.db3"

# 出力フォルダ（存在しなければ作成）
output_folder = "/Users/kaisei/Desktop/gaku-lala-apps/output_csv/"
os.makedirs(output_folder, exist_ok=True)

# SQLite に接続
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル一覧を取得
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📌 データベース内のテーブル一覧:")
for table in tables:
    print(f" - {table[0]}")

# すべてのテーブルをCSVに変換
for table in tables:
    table_name = table[0]
    print(f"🚀 {table_name} を CSV に変換中...")
    
    df = pd.read_sql(f"SELECT * FROM {table_name};", conn)
    output_path = os.path.join(output_folder, f"{table_name}.csv")
    
    df.to_csv(output_path, index=False)
    print(f"✅ 保存完了: {output_path}")

# SQLite 接続を閉じる
conn.close()
print("🎉 すべてのテーブルを CSV に変換完了！")
