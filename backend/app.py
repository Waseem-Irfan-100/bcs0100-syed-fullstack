from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student-details')
def details():
    return jsonify({
        "name": "Syed Waseem Irfan",
        "roll": "2023BCS0100",
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
