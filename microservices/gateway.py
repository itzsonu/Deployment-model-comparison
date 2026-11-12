from flask import Flask, jsonify
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/student', methods=['GET'])
def get_student():
    try:
        with urlopen('http://127.0.0.1:5001/student', timeout=3) as response:
            data = json.load(response)
        return jsonify(data)
    except Exception:
        return jsonify(error='Student service unavailable'), 503

if __name__ == '__main__':
    app.run(port=5002)