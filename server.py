from flask import Flask
import requests

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    jsonrequest = requests.json()
    first = jsonrequest['first']
    second = jsonrequest['second']
    result = first+second
    return result, 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    jsonrequest = requests.json()
    first = jsonrequest['first']
    second = jsonrequest['second']
    result = first-second
    return result, 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
