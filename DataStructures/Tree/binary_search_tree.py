from DataStructures.Tree import bst_node as n
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as al

def new_map():
    bst = {"root": None}
    return bst

def default_compare(key, element):
   if key == n.get_key(element):
      return 0
   elif key > n.get_key(element):
      return 1
   return -1

def get_node(node, key):
    """
    Busca un valor en el BST dado una llave.
    """
    current = node
    while current is not None:
        if key == current["key"]:
            return current["value"]  
        elif key < current["key"]:
            current = current["left"] 
        else:
            current = current["right"]  
    return None  

def insert_node(node, key, value):
    if node is None:
        return n.new_node(key, value)
    
    if key == node["key"]:
        node["value"] = value  
    elif key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)  
    else:
        node["right"] = insert_node(node["right"], key, value) 
        
    left_size = node["left"]["size"] if node["left"] else 0
    right_size = node["right"]["size"] if node["right"] else 0

    node["size"] = 1 + left_size + right_size
    
    return node

def get(bst, key):
    value = get_node(bst["root"], key)
    return value

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def delete_min_tree(node):
    if node is None:
        return None
    
    if node["left"] is None:
        return node["right"]  
    
    node["left"] = delete_min_tree(node["left"])  
    
    node["size"] -= 1
    
    return node
    
def delete_min(bst):
    bst["root"] = delete_min_tree(bst["root"])
    return bst

def delete_max_tree(node):
    if node is None:
        return None
    
    if node["right"] is None:
        return node["left"]  
    
    node["right"] = delete_min_tree(node["right"])  
    
    node["size"] -= 1
    
    return node
    
def delete_max(bst):
    bst["root"] = delete_max_tree(bst["root"])
    return bst

def remove_node(node, key):
 
    if node is None:
        return None
    
    if key < node["key"]:
        node["left"] = remove_node(node["left"], key)
    elif key > node["key"]:
        node["right"] = remove_node(node["right"], key)
    else:
       
        if node["right"] is None:
            return node["left"]
      
        if node["left"] is None:
            return node["right"]
        
       
        temp = node["right"]
        while temp["left"] is not None:
            temp = temp["left"]
        
   
        node["key"] = temp["key"]
        node["value"] = temp["value"]
        
     
        node["right"] = remove_node(node["right"], temp["key"])
    
    
    left_size = node["left"]["size"] if node["left"] else 0
    right_size = node["right"]["size"] if node["right"] else 0
    node["size"] = 1 + left_size + right_size
    
    return node

def remove(bst, key):
    bst['root'] = remove_node(bst['root'], key)
    return bst

def contains (bst,key):
    pass
        
def is_empty (bst):
    if bst["root"] == None:
        return True
    return False

def get_max (bst):
    maximo = max_key_node(bst["root"])
    return maximo

def min_key_node(node):
    if node is None:
        return None
    while node["left"] is not None:
        node = node["left"]
    return node["key"]

def max_key_node(node):
    if node is None:
        return None
    while node["right"] is not None:
        node = node["right"]
    return node["key"]

def get_min (bst):
    minimo  = min_key_node(bst["root"])
    return minimo

def floor_key(node, key):
    if node is None:
        return None
    
    if node["key"] == key:
        return node["key"]
    
    if key < node["key"]:
        return floor_key(node["left"], key)

    # Si la clave es mayor, puede que este nodo sea el floor, o esté más a la derecha
    temp = floor_key(node["right"], key)
    if temp is not None:
        return temp
    else:
        return node["key"]
        
def floor(my_bst, key):
    llave = floor_key(my_bst["root"], key)
    return llave

def size_tree(node):
    return node["size"] if node else 0
    
def size(bst):
    return size_tree(bst["root"])

def rank_keys(node, key):
    if node is None:
        return 0
    if node["key"] == key:
        return size_tree(node["left"])
    elif key < node["key"]:
        return rank_keys(node["left"], key)
    else:
        return 1 + size_tree(node["left"]) + rank_keys(node["right"], key)
    
def rank(bst, key):
    return rank_keys(bst["root"], key)

def height_tree(root):
    if root is None:
        return 0
    left = height_tree(root["left"])
    right = height_tree(root["right"])
    return 1 + max(left, right)

def height(my_bst):
    return height_tree(my_bst["root"])


def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return
    if key_initial < root["key"]:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= root["key"] <= key_final:
        sll.add_last(list_key, root["key"])  
    if key_final > root["key"]:
        keys_range(root["right"], key_initial, key_final, list_key)


def keys(my_bst, key_initial, key_final):
    result = sll.new_list()  
    keys_range(my_bst["root"], key_initial, key_final, result)  
    return result

def values_range(root, key_initial, key_final, list_values):
    if root is None:
        return
    if key_initial < root["key"]:
        values_range(root["left"], key_initial, key_final, list_values)
    if key_initial <= root["key"] <= key_final:
        sll.add_last(list_values, root["value"])
    if key_final > root["key"]:
        values_range(root["right"], key_initial, key_final, list_values)
        
def values(my_bst, key_initial, key_final):
    result = sll.new_list()
    values_range(my_bst["root"], key_initial, key_final, result)
    return result

def ceiling_key(node, key):
    if node is None:
        return None
    
    if node["key"] == key:
        return node["key"]
    
    if node["key"] < key:
        return ceiling_key(node["left"], key)
        
    if node["key"] > key:
        return ceiling_key(node["right"], key)
    
    right_floor = floor_key(node["right"], key)
    return right_floor if right_floor is not None else node["key"]
        
def ceiling(my_bst, key):
    llave = floor_key(my_bst["root"], key)
    return llave

def select(my_bst, pos):
    lista = al.new_list()
    lista = select_key(my_bst['root'], lista)
    if lista and pos < al.size(lista) and pos >= 0:
        key = al.get_element(lista, pos)
        return key["key"]
    else: return None
        

def select_key(root, lista):
    if root == None:
        return
    select_key(root['left'], lista)
    al.add_last(lista, root)
    select_key(root['right'], lista)
    
    return lista
    
def get_left(node):
    "Devuelve el nodo izquierdo"
    
    if node is None: return
    return node['left']

def get_right(node):
    "Devuelve el nodo derecho"
    
    if node is None: return
    return node['right']

def key_set(my_bst):
    curr = my_bst['root']
    keys = sll.new_list()
    curr = get_left(curr)
    if curr is not None:
        sll.add_last(keys, curr["key"])
    curr = get_right(curr)
    return keys
        

def value_set(my_bst):
    curr = my_bst['root']
    values = sll.new_list()
    curr = get_left(curr)
    if curr is not None:
        sll.add_last(values, curr["value"])
    curr = get_right(curr)
    return values

def contains(my_bst, key):
    if get(my_bst, key) == None:
        return False
    else: return True
    
"""
#PRUEBAS

# Crear BST nuevo
tree = new_map()

print("empty",is_empty(tree))  # True

# Insertar valores
put(tree, 10, "A")
put(tree, 5, "B")
put(tree, 15, "C")
put(tree, 3, "D")
put(tree, 7, "E")
put(tree, 12, "F")
put(tree, 18, "G")

# get
print("Obtener valor con clave 7:", get(tree, 7))  # "E"

# min y max
print("Clave mínima:", get_min(tree))  # 3
print("Clave máxima:", get_max(tree))  # 18

# floor
print("Floor de 13:", floor(tree, 13))  # 12


# size
print("Tamaño del árbol:", size(tree))  # 7

# rank
print("Rango de clave 12:", rank(tree, 12))  # 4 

# height
print("Altura del árbol:", height(tree))  # 3 

# keys en rango
rango_claves = keys(tree, 5, 15)
print("Claves entre 5 y 15:")


# values en rango
rango_valores = values(tree, 5, 15)
print("Valores entre claves 5 y 15:")


# delete_min
delete_min(tree)
print("Clave mínima después de eliminar la mínima:", get_min(tree))  # 5

# remove
remove(tree, 15)
print("Contiene 15 después de eliminarla:", get(tree, 15))  # None

# is_empty después de insertar
print("¿Árbol vacío ahora?", is_empty(tree))  # False
"""