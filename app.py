from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# 現在の時間を取得するAPI
@app.route("/")
def home():
    return "<h1>Flaskサーバー動作中</h1><p><a href='/time'>現在の時間を取得</a></p>"

@app.route('/time')
def get_time():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({"current_time": now})

# 名前を受け取って「Hello, ◯◯!」と返すAPI
@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/date")
def get_date():
    today = datetime.now().strftime("%Y-%m-%d")
    return jsonify({"date": today})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

# 売上データのサンプル
sample_data = [
    {"name": "1月", "売上": 4000, "利益": 2400, "コスト": 1600},
    {"name": "2月", "売上": 3000, "利益": 1398, "コスト": 1602},
    {"name": "3月", "売上": 2000, "利益": 800, "コスト": 1200},
    {"name": "4月", "売上": 2780, "利益": 1408, "コスト": 1372},
    {"name": "5月", "売上": 1890, "利益": 800, "コスト": 1090},
    {"name": "6月", "売上": 2390, "利益": 1200, "コスト": 1190},
    {"name": "7月", "売上": 3490, "利益": 2100, "コスト": 1390}
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sample_data)


