#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Toplam log sayı
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # HTTP metodları üzrə say
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET metodu və path = "/status" olanların sayı
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
