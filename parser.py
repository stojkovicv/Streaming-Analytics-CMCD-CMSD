import json

with open("./cmcd-server/access_cmcd.log", "r") as logfile:
    log_data = logfile.read()

log_data = log_data.replace("\\", "")
log_data = log_data.replace("}", "}, ")
log_data = log_data[:-1]
log_data = log_data[:-1]
log_data = log_data[:-1]
log_data = "[" + log_data + "]"
print(log_data)

log_json = json.loads(log_data)
print("\n")
# Connection with Mongodb cluster

# Uncomment next two lines to invoke pip installation of pymongo.
# import pip
# pip.main(["install", "pymongo"])
from pymongo import MongoClient

client = MongoClient("mongodb+srv://streaming654321:<PASSWORD>@cluster0.79v6jkt.mongodb.net/?retryWrites=true&w=majority")
print("Connection successful.")

db = client["streaming"]
collection = db["cmcds"]

for entry in log_json:
    collection.insert_one(entry)

print("Metrics inserted successfully.")
