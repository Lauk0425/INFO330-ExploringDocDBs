from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


print("Query")
query = {"name": "Pikachu"}
result = pokemonColl.find(query)
print(result)
    
print("Query1")
query1 = {"attack": {"$gt": 150}}
result1 = pokemonColl.find(query1)
for i in result1:
    print(i)
    
print("Query2")
query2 = {"ability": "Overgrow"}
result2 = pokemonColl.find(query2)
for j in result2:
    print(j)

