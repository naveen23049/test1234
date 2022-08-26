import pymongo


client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.ub7axwp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "Naveen",
    "email" : "naveen@12345",
    "surname" : "Thota"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)


