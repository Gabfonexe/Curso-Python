from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

post1 = {
  "title": "FastAPI",
  "Category": "Backend",
  "author": {
    "name": "Gabriel",
    "email": "gabriel@email.com"
  }    
}

result = mycol.insert_one(post1)
print("Documento incluído com sucesso")

