from flask import Flask
import request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    jsonrequest = request.json
    first = jsonrequest['first']
    second = jsonrequest['second']
    result = first+second
    return jsonify(result=result), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    jsonrequest = request.json
    first = jsonrequest['first']
    second = jsonrequest['second']
    result = first-second
    return jsonify(result=result), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
