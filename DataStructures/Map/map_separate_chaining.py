from DataStructures.Map import map_entry as e
from DataStructures.Map import map_functions as f
import random as r
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.List import list_node as n

def default_compare(key, element):
    if key == e.get_key(element):
        return 0
    elif key > e.get_key(element):
        return 1
    return -1

def new_map(num_elements, load_factor, prime=109345121):
    capacity = f.next_prime(int(num_elements / load_factor))
    scale = r.uniform(1, prime - 1)
    shift = r.uniform(0, prime - 1)

    tabla = al.new_list()
    for _ in range(capacity):
        al.add_last(tabla, sl.new_list())

    return {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": tabla,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }

def size(my_map):
    return my_map["size"]

def calc_currentfactor(size, capacity):
    return size / capacity

def put(my_map, key, value):
    pos = f.hash_value(my_map, key)
    pos_list = my_map["table"]["elements"][pos]
    size_list = pos_list["size"]
    current = pos_list["first"]

    found = False
    searchpos = 0
    while searchpos < size_list and not found:
        if current["info"]["key"] == key:
            sl.change_info(pos_list, searchpos, e.new_map_entry(key, value))
            found = True
        else:
            current = current["next"]
            searchpos += 1

    if not found:
        sl.add_last(pos_list, e.new_map_entry(key, value))
        my_map["size"] += 1

    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)

    return my_map

def get(my_map, key):
    pos = f.hash_value(my_map, key)
    pos_list = my_map["table"]["elements"][pos]
    current = pos_list["first"]
    size_list = pos_list["size"]
    searchpos = 0

    while searchpos < size_list:
        if current["info"]["key"] == key:
            return current["info"]["value"]
        current = current["next"]
        searchpos += 1
    return None

def contains(my_map, key):
    return get(my_map, key) is not None

def remove(my_map, key):
    pos = f.hash_value(my_map, key)
    pos_list = my_map["table"]["elements"][pos]
    current = pos_list["first"]
    size_list = pos_list["size"]
    searchpos = 0
    found = False

    while searchpos < size_list and not found:
        if current["info"]["key"] == key:
            sl.delete_element(pos_list, searchpos)
            my_map["size"] -= 1
            found = True
        else:
            current = current["next"]
            searchpos += 1

    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map

def is_empty(my_map):
    return my_map["size"] == 0

def key_set(my_map):
    keys = al.new_list()
    for slot in my_map["table"]["elements"]:
        current = slot["first"]
        while current is not None:
            al.add_last(keys, current["info"]["key"])
            current = current["next"]
    return keys

def value_set(my_map):
    values = al.new_list()
    for slot in my_map["table"]["elements"]:
        current = slot["first"]
        while current is not None:
            al.add_last(values, current["info"]["value"])
            current = current["next"]
    return values

def rehash(my_map):
    nueva_capacidad = f.next_prime(int(my_map["capacity"] * 2))
    nueva_tabla = al.new_list()

    for _ in range(nueva_capacidad):
        al.add_last(nueva_tabla, sl.new_list())

    elementos_actuales = my_map["table"]["elements"]

    my_map["table"] = nueva_tabla
    my_map["capacity"] = nueva_capacidad
    my_map["size"] = 0

    for casilla in elementos_actuales:
        nodo = casilla["first"]
        while nodo is not None:
            entrada = nodo["info"]
            llave = entrada["key"]
            valor = entrada["value"]
            put(my_map, llave, valor)
            nodo = nodo["next"]

    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map



#PRUEBAS
my_table = new_map(5, 0.5, 7)
print(my_table)
# Salida esperada la misma respuesta de la función new_map()

# Agregar un nuevo elemento a la tabla
my_table = put(my_table, 1, {'name': 'John', 'age': 25})
my_table = put(my_table, 2, {'name': 'gaby', 'age': 25})
print("PUT", my_table)

my_table = remove(my_table, 1)
# Verificar si la llave 1 se encuentra en la tabla

print(contains(my_table, 1))
print(contains(my_table, 2))
print(value_set(my_table))
print(key_set(my_table))
print(is_empty(my_table))
print(rehash(my_table))

# Salida esperada: True

# Verificar si la llave 2 se encuentra en la tabla
#print(contains(my_table, 2))
#print(get(my_table, 1))

