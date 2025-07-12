#!/usr/bin/env python3
'''Task 11'''

def schools_by_topic(mongo_collection, topic):
    '''Task 11'''
    return list(mongo_collection.find({ "topics": topic }))
