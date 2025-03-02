from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import matplotlib
matplotlib.rcParams['font.family'] = 'Arial'  # 'IPAexGothic' にすると日本語もOK


# Mac のクラッシュ回避用
matplotlib.use("Agg")

app = Flask(__name__)
CORS(app)  # CORSを適用

# CSVファイルのパス
CSV_FILE = "quote.csv"

# データ読み込み
df = pd.read_csv(CSV_FILE, dtype=str)  # すべて文字列として読む

# **日付フォーマットを統一**
df["YYYY/MM/DD"] = df["YYYY/MM/DD"].astype(str).apply(lambda x: pd.to_datetime(x).strftime("%Y/%m/%d"))

@app.route("/")
def home():
    return "<h1>為替データダッシュボード</h1><p><a href='/dashboard'>ダッシュボード</a></p>"

@app.route("/dashboard")
def dashboard():
    data = df.to_dict(orient="records")
    return render_template("dashboard.html", data=data)

@app.route("/quotes", methods=["GET"])
def get_quote_data():
    date = request.args.get("date")  # 例: /quotes?date=2024/02/26
    print(f"🔍 リクエストされた日付: {date}")  

    if date in df["YYYY/MM/DD"].values:
        data = df[df["YYYY/MM/DD"] == date].to_dict(orient="records")
        print(f"📊 取得データ: {data}")  
        return jsonify(data)
    else:
        return jsonify({"error": "指定した日付のデータがありません"})

@app.route("/plot/usd")
def plot_usd():
    """USD/JPY の為替推移を改善したデザインで描画"""
    df["YYYY/MM/DD"] = pd.to_datetime(df["YYYY/MM/DD"])
    df_sorted = df.sort_values("YYYY/MM/DD")

    plt.figure(figsize=(10, 5))
    plt.plot(df_sorted["YYYY/MM/DD"], df_sorted["USD米ドル"], marker="o", linestyle="-", color="blue", markersize=4)
    plt.xlabel("日付", fontsize=12)
    plt.ylabel("USD/JPY", fontsize=12)
    plt.title("USD/JPY 為替推移", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)

    img = io.BytesIO()
    plt.savefig(img, format="png", bbox_inches="tight", dpi=150)
    img.seek(0)
    return Response(img.getvalue(), mimetype="image/png")

@app.route("/api/usd")
def api_usd():
    """JSON形式でUSD/JPYのデータを提供"""
    df["YYYY/MM/DD"] = pd.to_datetime(df["YYYY/MM/DD"])
    df_sorted = df.sort_values("YYYY/MM/DD")

    data = [
        {"date": row["YYYY/MM/DD"].strftime("%Y-%m-%d"), "value": row["USD米ドル"]}
        for _, row in df_sorted.iterrows()
    ]

    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
