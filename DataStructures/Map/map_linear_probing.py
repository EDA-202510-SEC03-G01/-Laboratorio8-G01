######
from DataStructures.Map import map_entry as e
from DataStructures.Map import map_functions as f
import random as r
from DataStructures.List import array_list as al

#import map_entry as e
#import map_functions as f
#from ..List import array_list as al
#UNO
def new_map(num_elements, load_factor, prime=109345121):
    # Se crean los atributos iniciales
    capacity = f.next_prime(num_elements/load_factor)
    
    # Se importa random para obtener numeros aleatorios dentro del rango
    scale = r.uniform(1, prime-1)
    shift = r.uniform(0, prime-1)
    
    # Se crea la tabla y se usa un loop para obtener la cantidad necesaria
    # de elementos vacios
    tabla = al.new_list()
    for x in range(capacity):
        al.add_last(tabla, e.new_map_entry(None,None))
    
    map = {"prime": prime,
     "capacity": capacity,
     "scale": scale,
     "shift": shift,
     "table":tabla,
     "current_factor": 0,
     "limit_factor": load_factor,
     "size":0
    }
    return map

def size (map):
    return map["size"]

#######








#######
def calc_currentfactor(size, capacity):
    return size/capacity

def contains(my_map, key):
    hash_el = f.hash_value(my_map, key)
    pos = f.find_slot(my_map, key, hash_el)
    if key == my_map["table"]["elements"][pos[1]]["key"]:
            return True
    return False

def put(my_map, key, value):
    if contains(my_map, key) == False:
        hash_el = f.hash_value(my_map, key)
        pos = f.find_slot(my_map, key, hash_el)
        #print("elemento",my_map["table"]["elements"][pos[1]]["key"])
        my_map["table"]["elements"][pos[1]]["key"] = key
        my_map["table"]["elements"][pos[1]]["value"] = value
        my_map["size"] += 1
        my_map["current_factor"] = calc_currentfactor(my_map["size"], my_map["capacity"])
    else:
        hash_el = f.hash_value(my_map, key)
        pos = f.find_slot(my_map, key, hash_el)
        my_map["table"]["elements"][pos[1]]["value"]= value
        my_map["current_factor"] = calc_currentfactor(my_map["size"], my_map["capacity"])
    return my_map

def get(my_map, key):
    val = None
    hash_value = f.hash_value(my_map, key)
    pos = f.find_slot(my_map, key, hash_value)
    if key == my_map["table"]["elements"][pos[1]]["key"]:
        val = my_map["table"]["elements"][pos[1]]["value"]
        return val
    return None

def is_empty(my_map):
    if my_map["size"] == 0:
        return True
    return False

def key_set(my_map):
    array = al.new_list()
    for i in range(my_map["table"]["size"]):
        key = my_map["table"]["elements"][i]["key"]
        if key is not None:
            array = al.add_last(array,key)
    return array

def value_set(my_map):
    array = al.new_list()
    for i in range(my_map["table"]["size"]):
        value = my_map["table"]["elements"][i]["value"]
        if value is not None:
            array = al.add_last(array,value)
    return array

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if e.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):

   entry = al.get_element(table, pos)
   if e.get_key(entry) is None or e.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == e.get_key(entry):
      return 0
   elif key > e.get_key(entry):
      return 1
   return -1

def rehash(my_map):
    n = my_map["table"]["size"] 
    nuevo_map = new_map(n, my_map["limit_factor"])
    for i in my_map["table"]["elements"]:
        if i["key"] is not None: 
            put(nuevo_map, i["key"], i["value"])
    my_map = nuevo_map
    return nuevo_map


def remove(my_map, key):
    hash_value = f.hash_value(my_map, key)
    pos = f.find_slot(my_map, key, hash_value)
    if get(my_map,key) is not None:
        put(my_map, key, None)
        my_map["table"]["elements"][pos[1]]["key"] = None
        my_map["size"] -= 1
        my_map["current_factor"] = calc_currentfactor(my_map["size"], my_map["capacity"])
    return my_map
        
########









########
#TRES

"""
def get(my_map, key):
    val = None
    hash_value = f.hash_value(my_map["table"], key)
    pos = f.find_slot(my_map, key, hash_value)
    if key == al.get_element(my_map["table"]["elements"],pos)["key"]:
        val = al.get_element(my_map["table"]["elements"],pos)["value"]
    return val


def remove(my_map, key):
    hash_value = f.hash_value(my_map["table"], key)
    pos = f.find_slot(my_map, key, hash_value)
    if key == al.get_element(my_map["table"]["elements"],pos)["key"]:
        al.get_element(my_map["table"]["elements"],pos)["key"] = None
        al.get_element(my_map["table"]["elements"],pos)["Value"] = None
    return my_map
     









#PRUEBAS
my_table = new_map(5, 0.5)
#print(my_table) # Se espera la misma respuesta de new_map()

# Agregar varios elementos a la tabla
my_table = put(my_table, 1, {'name': 'John', 'age': 25})
my_table = put(my_table, 3, {'name': 'Jane', 'age': 22})
my_table = put(my_table, 5, {'name': 'Doe', 'age': 30})
my_table = put(my_table, 8, {'name': 'Mary', 'age': 20})
print("TABLA",my_table)
my_table = remove(my_table, 3)
print("BORRADO", my_table)

# Obtener el conjunto de llaves de la tabla
#print(key_set(my_table))
#print(value_set(my_table))
#print(remove(my_table,3))
"""
my_table = new_map(5, 0.5)
print(my_table) # Se espera la misma respuesta de new_map()

# Agregar varios elementos a la tabla
my_table = put(my_table, 1, {'name': 'John', 'age': 25})
my_table = put(my_table, 3, {'name': 'Jane', 'age': 22})
my_table = put(my_table, 5, {'name': 'Doe', 'age': 30})
my_table = put(my_table, 8, {'name': 'Mary', 'age': 20})
print(my_table)

# Realizar un rehash de la tabla
my_table = rehash(my_table)
print(my_table)
print(f.next_prime(11*2))