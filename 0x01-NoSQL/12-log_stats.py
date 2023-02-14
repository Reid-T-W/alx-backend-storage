#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in
MonogDB
"""
import pymongo


# Establishing connection to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Getting db
db = client["logs"]

# Collection name
col = db["nginx"]

print(f"{col.count_documents({})} logs")
print("Methods:")
print(f"    method GET: {col.count_documents({'method': 'GET'})}")
print(f"    method POST: {col.count_documents({'method': 'POST'})}")
print(f"    method PUT: {col.count_documents({'method': 'PUT'})}")
print(f"    method PATCH: {col.count_documents({'method': 'PATCH'})}")
print(f"    method DELETE: {col.count_documents({'method': 'DELETE'})}")
print("{} status check".
      format(col.count_documents({'method': 'GET', 'path': '/status'})))
