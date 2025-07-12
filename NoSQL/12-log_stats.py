#!/usr/bin/env python3
'''Task 12'''

from pymongo import MongoClient

def print_nginx_stats():
    '''Task 12'''
    client = MongoClient()
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({ "method": method })
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({ "method": "GET", "path": "/status" })
    print(f"{status_check} status check")

if __name__ == "__main__":
    print_nginx_stats()
