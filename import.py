import sqlite3  # This is the package for all sqlite3 access in Python
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()
query1 = """
SELECT COUNT(*)
FROM pokemon as p
"""
# setup for query1
query1_result = c.execute(query1)
print(query1_result)
pokemon_table = c.fetchone()
id_num = pokemon_table[0]


for i in range(1, id_num + 1):
    #query for all the information needed in the pokemon table
    pokemon_table = """
     SELECT p.id, p.name, p.pokedex_number, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense
     FROM pokemon as p
     """
    p_table_result = c.execute(pokemon_table)
    # print(p_table_result)
    pokemon_result = c.fetchone()
    

    type_table = "SELECT pt.pokemon_id, pt.type_id, t.name, t.id FROM pokemon_type as pt JOIN type as t on pt.type_id = t.id WHERE pt.pokemon_id = " + str(i) + ";"
    
    type_table_result = c.execute(type_table)
    # print(type_table_result)
    type_result = type_table_result.fetchall()
    type_list = [type_result[0][2], type_result[1][2]]
    # print(type_list)

    ability_table = "SELECT p.pokemon_id, a.id, a.name FROM pokemon_abilities as p JOIN ability as a on p.ability_id = a.id WHERE p.pokemon_id = " + str(i) + ";"
    ability_table_result = c.execute(ability_table)
    ability_result = ability_table_result.fetchall()
    new_list = []
    for j in ability_result:
        new_list.append(j[2])
        print(new_list)
   

    pokemon = {
    "name": pokemon_result[2],
    "pokedex_number": pokemon_result[1],
    "types": type_list,
    "hp": pokemon_result[3],
    "attack": pokemon_result[4],
    "defense": pokemon_result[5],
    "speed": pokemon_result[6],
    "sp_attack": pokemon_result[7],
    "sp_defense": pokemon_result[8],
    "abilities": new_list
    }
    pokemonColl.insert_one(pokemon) 




    

    


