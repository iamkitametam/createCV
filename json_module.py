import json
import codecs
from pymongo import MongoClient


person = {
    "FIO" : FIO,
    "salary" : salary,
    "jobs" : jobs_return,
    "educations" : educations_return,
    "additional_educations" : additional_educations_return,
    "languages" : languages,
    "photo_url" : photo_url,
    "birth_date" : birth_date,
    "location" : location
}

# write to file

# with codecs.open("data_file.txt", "w", encoding='utf-8') as write_file:
#     json.dump(person, write_file, ensure_ascii=False)

# write to mongo database

# try:
#     conn = MongoClient()
#     print("Connected successfully!!!")
# except:
#     print("Could not connect to MongoDB")
#
# # database
# db = conn.database
#
# # Created or Switched to collection names: my_gfg_collection
# collection = db.candidates
#
# # Insert Data
# rec_id = collection.insert_one(person)
#
# print("Data inserted with record id", rec_id)
#
# # Printing the data inserted
# cursor = collection.find()
# for record in cursor:
#     print(record)