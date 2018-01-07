# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import json

with open('crawler/infoq.json', 'r', encoding='utf-8') as f:
    data = json.load(f);

client = MongoClient()
db = client.ainext

infoq = db.infoq
infoq.insert_many(data)
