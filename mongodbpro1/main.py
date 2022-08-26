import pymongo



client = pymongo.MongoClient("mongodb+srv://naveen45:mongodb@cluster0.bsmjvfo.mongodb.net/?retryWrites=true&w=majority")
db = client.test


data = {
    "name" : "Naveen",
    "mail_id" : "naveen@xyz",
    "subject" : ["data science","data analytics"]
}

database = client['myinfo']
collection = database["cat"]
collection.insert_one(data)