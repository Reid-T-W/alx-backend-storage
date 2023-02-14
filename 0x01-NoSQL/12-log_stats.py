#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in
MonogDB
"""
import pymongo


if __name__ == "__main__":
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Getting db
    db = client["logs"]

    # Collection name
    col = db["nginx"]

    print(f"{col.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {col.count_documents({'method': 'GET'})}"
          .expandtabs(4))
    print(f"\tmethod POST: {col.count_documents({'method': 'POST'})}"
          .expandtabs(4))
    print(f"\tmethod PUT: {col.count_documents({'method': 'PUT'})}"
          .expandtabs(4))
    print(f"\tmethod PATCH: {col.count_documents({'method': 'PATCH'})}"
          .expandtabs(4))
    print(f"\tmethod DELETE: {col.count_documents({'method': 'DELETE'})}"
          .expandtabs(4))
    print("{} status check".
          format(col.count_documents({'method': 'GET', 'path': '/status'})))
