import pymongo
from urllib.parse import quote_plus
import datetime


username = quote_plus('Dorsa')

password = quote_plus('123456789Dorsa')

cluster = 'Cluster0'

authSource = 'ddnxd.mongodb.net'

authMechanism = 'DEFAULT'

uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism

client = pymongo.MongoClient(uri)

# db = client.gettingStarted

# people = db.people

# personDocument = {
#   "name": { "first": "Alan", "last": "Turing" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }
# people.insert_one(personDocument)

# result = client["<dbName"]["<collName>"].find()


# for i in result:

#     print(i)