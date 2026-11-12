from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student', methods=['GET'])
def student():
    return jsonify(studentId='134', name='Mritunjai', course='MCA')

if __name__ == '__main__':
    app.run(port=5001)