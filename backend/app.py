from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details', methods=['GET'])
def get_details():
    data = {
        "name": "Syed Waseem Irfan",
        "roll": "2023BCS0100",
        "register": "100"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)