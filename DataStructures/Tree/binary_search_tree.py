from DataStructures.Tree import bst_node as n

def new_map():
    bst = {"root": None}
    return bst

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

def min_key_node(node):
    if node is None:
        return None
    while node is not None:
        node = node["left"]
    return node["key"]

def min_key(bst):
    min  = min_key_node(bst["root"])
    return min

def floor_key(node, key):
    if node is None:
        return None
    
    if node["key"] == key:
        return node["key"]
    
    if node["key"] > key:
        return floor_key(node["left"], key)
        
    if node["key"] < key:
        return floor_key(node["right"], key)
    
    right_floor = floor_key(node["right"], key)
    return right_floor if right_floor is not None else node["key"]
        
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
    return rank_keys(bst["root"], key, bst["cmp_function"])