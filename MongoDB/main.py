import random
from pymongo import MongoClient
import local_settings

client = MongoClient(host=local_settings.DATABASE['host'], port=local_settings.DATABASE['port'])

mongodb_database = client[local_settings.DATABASE['name']]

# Create or get the "Information" collection
information_collection = mongodb_database.get_collection('Information')

# Create or get the "Phone" collection
phone_collection = mongodb_database.get_collection('Phone')

first_names = ['Ali', 'Amir', 'Hadi', 'Omid', 'Maryam', 'Reza', 'Sara', 'Zahra']
last_names = ['Ahmadi', 'Amiri', 'rezai', 'Omidi', 'Maryami', 'Mohamadi', 'Hashemi', 'Nasiri']

# Generate sample data for "Information" collection
information_data = [
    {"_id": i, "first_name": random.choice(first_names), "last_name": random.choice(last_names),
     "address": f"Address {i}"}
    for i in range(100)
]

# Insert sample data into "Information" collection
result_info = information_collection.insert_many(information_data)
print(result_info.inserted_ids)

# Generate sample data for "Phone" collection with foreign key referencing "Information" collection
phone_data = [
    {"phone_number": f"123456789{i}", "information_id": i}
    for i in range(100)
]

# Insert sample data into "Phone" collection
result_phone = phone_collection.insert_many(phone_data)
print(result_phone.inserted_ids)

random_last_name = random.choice(last_names)
print("Random Last Name:", random_last_name)

# Query "Information" collection to find matching last name
info_query = {"last_name": random_last_name}
information = information_collection.find(info_query)

# For each matching document in "Information" collection, find corresponding phone numbers in "Phone" collection
for i, info in enumerate(information):
    phone_query = {"information_id": info["_id"]}
    phones = phone_collection.find(phone_query)

    print(f"\nInformation {i}:")
    print(info)

    print("Phones:")
    for phone in phones:
        print(phone)
