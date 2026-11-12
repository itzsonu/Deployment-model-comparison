from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/student')
def student():
    return jsonify(studentId='134', name='Mritunjai', course='MCSA')

if __name__ == '__main__':
    app.run(port=5000)