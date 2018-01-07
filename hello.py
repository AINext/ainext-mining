from flask import Flask
import json
from pprint import pprint
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello():
    client = MongoClient()
    db = client.ainext
    infoq = db.infoq

    html = ""
    count = 0
    for item in infoq.find():
        html = html + "<p>"+ item['title'] +"</p>"
        if count <10 :
            html = html + "<p>" + item['content'] + "</p>"
        html = html + "<hr>"
        count = count + 1
    return html;

app.run(host='0.0.0.0', port=5000)
