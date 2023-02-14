#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection
    Args:
        mongo_collection: collection to be queried
    Return:
        List of all documents in a collection
        An empty list is returned if no document is in the collection
    """
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Database name
    # db = client["my_db"]

    # Collection name
    # col = db["school"]

    # Retrieving and returning the documents
    # Checking if the collection has no documents
    # if mongo_collection.count_documents == 0:
    #    return []
    return [doc for doc in mongo_collection.find()]
