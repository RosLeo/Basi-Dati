import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ZARA"]
mycol = mydb["zara_data"]

#query per convertire i prezzi da stringa a double
'''
pipeline = [{"$set": {"price": { "$toDouble": "$price" }}}]

mycol.update_many({}, pipeline)
'''

#query sulla colonna availability per sostituire le stringhe "" con "NotStock"
'''
query = { "availability": { "$eq": "" } }

new_values = { "$set": { "availability": "NotStock" } }

result = mycol.update_many(query, new_values)
'''

#elimino la colonna images
'''
query = {}
new_values = { "$unset": { "images": 1 } }  # Imposta il valore 1 per eliminare completamente la colonna

result = mycol.update_many(query, new_values)
'''

#elimino la colonna condition
'''
query = {}
new_values = { "$unset": { "condition": 1 } }  # Imposta il valore 1 per eliminare completamente la colonna

result = mycol.update_many(query, new_values)
'''

#elimino la colonna mpn
'''
query = {}
new_values = { "$unset": { "mpn": 1 } }  # Imposta il valore 1 per eliminare completamente la colonna

result = mycol.update_many(query, new_values)
'''

#elimino la colonna currency (valuta)
'''
query = {}
new_values = { "$unset": { "currency": 1 } }  # Imposta il valore 1 per eliminare completamente la colonna

result = mycol.update_many(query, new_values)
'''

#query sulla colonna size_list per sostituire la stringa "" con "S/M/L/XL"
'''
query = { "size_list": { "$eq": "" } }

# Nuovi valori da impostare per la colonna "availability"
new_values = { "$set": { "size_list": "S/M/L/XL" } }

# Esegui l'aggiornamento delle righe
result = mycol.update_many(query, new_values)
'''

#Query che fa in modo che in corrispondeza delle righe "NotStock" ci sia un valore in size_list "Unavailable"
'''
query = {"availability": {"$regex": "NotStock","$options": "i"}}

new_values = {"$set": {"size_list": "Unavailable"}}

result = mycol.update_many(query, new_values)
'''

#Query che estrapola tutte le differenti taglie della colonna size list oppure color o
'''
distinct_sizes_query = [
    {
        "$group": {
            "_id": None,
            "sizes": {"$addToSet": "$color"}
        }
    }
]

result = mycol.aggregate(distinct_sizes_query)

# Ottieni l'elenco delle taglie distinte
distinct_sizes = next(result, {}).get("sizes", [])

print(distinct_sizes)
'''

