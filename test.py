from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
from konlpy.tag import Kkma
from konlpy.utils import pprint
from words import summerize
import json
import jpype

kkma = Kkma()
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello."

@app.route("/test", methods=['GET','POST'])
def test():
    if request.method == 'GET':
        return 'get test'
    if request.method == 'POST':
        f = open("/home/ubuntu/test/text/test.txt",'a')
        id = request.form['id']
        f.write(id)
        return 'save success'

@app.route("/returnresult",methods=['GET','POST'])
def returnresult():
    if request.method == 'POST':
        id = request.form['action']
        jpype.attachThreadToJVM()
        result = summerize.summerize()
        return result.returnResult()

@app.route("/returncount", methods=['POST'])
def returncount():
    if request.method == 'POST':
        id = request.form['action']
        jpype.attachThreadToJVM()
        result = summerize.summerize()
        return json.dumps(result.returnWordCount(),ensure_ascii=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
