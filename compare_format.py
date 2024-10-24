import json
from fastavro import parse_schema, writer, reader
import io
import sys
import time
import random
import string
import person_pb2  # Assurez-vous que person_pb2.py est généré
import gc  # Pour le ramasse-miettes
import tracemalloc  # Pour mesurer la consommation mémoire

# Classe Personne
class Personne:
    def __init__(self, name, age, active, hobbies):
        self.name = name
        self.age = age
        self.active = active
        self.hobbies = hobbies

def generate_random_person():
    name = ''.join(random.choices(string.ascii_letters, k=10))
    age = random.randint(1, 100)
    active = random.choice([True, False])
    hobbies = [''.join(random.choices(string.ascii_letters, k=8)) for _ in range(random.randint(1, 5))]
    return Personne(name, age, active, hobbies)

# Générer une liste de 1 000 000 personnes
print("Génération des données...")
personnes = [generate_random_person() for _ in range(100000)]

# Fonction pour mesurer la consommation mémoire
def measure_memory():
    gc.collect()
    return tracemalloc.get_traced_memory()[1]

# Démarrer le traçage de la mémoire
tracemalloc.start()

# --- Protobuf ---
print("\n--- Protobuf ---")
start_time = time.time()

# Création de l'instance PersonList
person_list_proto = person_pb2.PersonList()
for personne in personnes:
    person_proto = person_list_proto.people.add()
    person_proto.name = personne.name
    person_proto.id = personne.age
    person_proto.active = personne.active
    person_proto.hobbies.extend(personne.hobbies)

serialization_time = time.time() - start_time
serialized_proto = person_list_proto.SerializeToString()
size_proto = len(serialized_proto)
memory_usage_proto = measure_memory()

print(f"Protobuf serialization size: {size_proto} bytes")
print(f"Protobuf serialization time: {serialization_time:.2f} seconds")
print(f"Protobuf memory usage: {memory_usage_proto / (1024 * 1024):.2f} MB")

# Désérialisation Protobuf
start_time = time.time()
deserialized_proto = person_pb2.PersonList()
deserialized_proto.ParseFromString(serialized_proto)
deserialization_time = time.time() - start_time
print(f"Protobuf deserialization time: {deserialization_time:.2f} seconds")

# Réinitialiser le traçage de la mémoire
tracemalloc.reset_peak()

# --- JSON ---
print("\n--- JSON ---")
start_time = time.time()

# Création de la liste de dictionnaires
personnes_dict = [{
    "name": personne.name,
    "age": personne.age,
    "active": personne.active,
    "hobbies": personne.hobbies
} for personne in personnes]

serialization_time_data_prep = time.time() - start_time

start_time = time.time()
json_string = json.dumps(personnes_dict, separators=(',', ':'))
serialization_time_json = time.time() - start_time

serialization_time = serialization_time_data_prep + serialization_time_json
serialized_json = json_string.encode('utf-8')
size_json = len(serialized_json)
memory_usage_json = measure_memory()

print(f"JSON serialization size: {size_json} bytes")
print(f"JSON serialization time: {serialization_time:.2f} seconds")
print(f"JSON memory usage: {memory_usage_json / (1024 * 1024):.2f} MB")

# Désérialisation JSON
start_time = time.time()
deserialized_json_list = json.loads(json_string)
deserialization_time = time.time() - start_time
print(f"JSON deserialization time: {deserialization_time:.2f} seconds")

# Réinitialiser le traçage de la mémoire
tracemalloc.reset_peak()

# --- Avro avec fastavro ---
print("\n--- Avro (fastavro) ---")
start_time = time.time()

# Définition du schéma Avro
avro_schema = {
    "type": "record",
    "name": "PersonList",
    "fields": [
        {
            "name": "people",
            "type": {
                "type": "array",
                "items": {
                    "type": "record",
                    "name": "Person",
                    "fields": [
                        {"name": "name", "type": "string"},
                        {"name": "age", "type": "int"},
                        {"name": "active", "type": "boolean"},
                        {"name": "hobbies", "type": {"type": "array", "items": "string"}}
                    ]
                }
            }
        }
    ]
}

parsed_schema = parse_schema(avro_schema)

# Préparation des données
data = {
    "people": [{
        "name": personne.name,
        "age": personne.age,
        "active": personne.active,
        "hobbies": personne.hobbies
    } for personne in personnes]
}

serialization_time_data_prep = time.time() - start_time

# Sérialisation Avro avec fastavro
start_time = time.time()
avro_bytes_io = io.BytesIO()
writer(avro_bytes_io, parsed_schema, [data])  # Notez que les données doivent être dans une liste
serialization_time_avro = time.time() - start_time

serialization_time = serialization_time_data_prep + serialization_time_avro
serialized_avro = avro_bytes_io.getvalue()
size_avro = len(serialized_avro)
memory_usage_avro = measure_memory()

print(f"Avro (fastavro) serialization size: {size_avro} bytes")
print(f"Avro (fastavro) serialization time: {serialization_time:.2f} seconds")
print(f"Avro (fastavro) memory usage: {memory_usage_avro / (1024 * 1024):.2f} MB")

# Désérialisation Avro avec fastavro en utilisant un générateur
start_time = time.time()
avro_bytes_io.seek(0)
deserialized_records = (record for record in reader(avro_bytes_io))
# Traitez les enregistrements au fur et à mesure sans les stocker tous
for record in deserialized_records:
    # Traitez chaque record ici
    pass
deserialization_time = time.time() - start_time
print(f"Avro (fastavro) deserialization time: {deserialization_time:.2f} seconds")


# Arrêter le traçage de la mémoire
tracemalloc.stop()

# Vérification de la désérialisation
print("\nDeserialization successful")
