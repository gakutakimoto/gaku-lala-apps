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



