from DataStructures.List import list_node as node
#import list_node as node


#FUNCIONES BÁSICAS LL LAB4 
def new_list():
    newlist = {
        "first": None,
        "last":None,
        "size":0,
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

lista = new_list()

def add_first(my_list, element):

    new_node = node.new_single_node(element)  

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node  

    my_list["size"] += 1 
    
    return my_list
#print("primero", add_first(lista,1))
#print(add_first(lista,4))
# Salida esperada:
# {'size': 1,
#  'first': {'info': 1, 'next': None},
#  'last': {'info': 1, 'next': None}
# }
def add_last(my_list, element):
    new_node = node.new_single_node(element) 
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = None
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list
#print(add_last(lista,2))
#print(add_last(lista,3))

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
#print(is_empty(lista))   

def first_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        primero = my_list["first"]["info"]
        return primero
#print(first_element(lista))

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        ultimo = my_list["last"]["info"]
        return ultimo
#print(last_element(lista))


def get_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    else: 
        actual = my_list["first"]
        for _ in range(pos):
            actual = actual["next"]
        return actual["info"]
#print("get_element",get_element(lista, 0))

def size(my_list):
    return my_list["size"]

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        if pos == 0:
            my_list["first"] = my_list["first"]["next"]
            
        else:
            actual = my_list["first"]
            for _ in range(pos-1):
                actual = actual["next"]
            elemento_borrar = actual["next"]
            actual["next"] = elemento_borrar["next"]
        my_list["size"] -= 1
        return my_list
#print(delete_element(lista, 0))

def remove_first(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    else:
        info = my_list["first"]["info"]
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        return info
#print(remove_first(lista))    

def remove_last(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    else:
        actual = my_list["first"]
        para_borrar = my_list["last"]["info"]
        for _ in range(size(my_list)-1):
            actual = actual["next"]
        my_list["last"] = actual
        my_list["size"] -= 1
        return para_borrar
    
def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        actual = my_list["first"]
        
        new_node = node.new_single_node(element)  
        if pos == 0:
            primero =  my_list["first"]
            my_list["first"] = new_node
            new_node["next"] = primero
        else:
            for _ in range(pos):
                prev = actual
                actual = actual["next"]
                
            prev["next"] = new_node
            new_node["next"] = actual
            my_list["size"] += 1
        return my_list
#print(insert_element(lista,"gabi", 0))     
#print(insert_element(lista,"chao", 1))  
#print(insert_element(lista,"l", 0))     
#print(insert_element(lista,"ch", 1)) 

 
            
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        actual = my_list["first"]
        for _ in range(pos):
            actual = actual["next"]
        
        actual["info"] = new_info
        return my_list
    
#print(change_info(lista, 1, "Hola"))

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        prev_pos1 = None
        prev_pos2 = None
         
        if pos_1 > pos_2:
            pos_1, pos_2 = pos_2, pos_1
        
        if pos_1 == pos_2:
            return my_list
    
        actual_pos1 = my_list["first"]
        actual_pos2 = my_list["first"]
        
        for _ in range(pos_1):
            prev_pos1 = actual_pos1
            actual_pos1 = actual_pos1["next"]
        
        for _ in range(pos_2):
            prev_pos2 = actual_pos2
            actual_pos2 = actual_pos2["next"]
        
      
        if pos_1 == 0:
            my_list["first"] = actual_pos2
        else:
            prev_pos1["next"] = actual_pos2
        
        prev_pos2["next"] = actual_pos1
        
        temp = actual_pos1["next"]
        actual_pos1["next"] = actual_pos2["next"]
        actual_pos2["next"] = temp
        
        return my_list
#print("exchange",exchange(lista, 0,1))     

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    if num_elements <= 0:
        return new_list()
    else:  
        sub_lista = new_list()
        actual = my_list["first"]
        for _ in range(pos):
            actual = actual["next"]
    
        for _ in range(num_elements):
            if actual is None:
                break
            add_last(sub_lista, actual["info"])
            actual = actual["next"]
    
        return sub_lista
#print(sub_list(lista, 1,2))
            
#FUNCIONES LAB5 ORDENAMIENTO
def default_sort_criteria(element_1, element_2):
    #RETORNA TRUE SI ELEMENT1 DEBE IR ANTES DEL 2
   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def insertion_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list
    
    lista_ordenada = new_list()
    current = my_list["first"]
    
    while current != None:
        valor = current["info"]
        new_node = {"info": valor, "next": None}
        if lista_ordenada["size"] == 0:
            lista_ordenada["first"] = new_node
            lista_ordenada["last"] = new_node
            lista_ordenada["size"] += 1 
        else:
            if sort_crit(valor, lista_ordenada["first"]["info"]):
                #Si valor debe ir antes del que esta de primero
                new_node["next"] = lista_ordenada["first"]
                lista_ordenada["first"] = new_node
                lista_ordenada["size"] += 1
            else:
                #el valor debe ir mas adelante que el primero
                prev = None
                current_sorted = lista_ordenada["first"]

                while current_sorted is not None and sort_crit(valor, current_sorted["info"]) != True:
                    prev = current_sorted
                    current_sorted = current_sorted["next"]

                #se añade el nodo entre prev y current sorted
                new_node["next"] = current_sorted
                prev["next"] = new_node
                lista_ordenada["size"] += 1

                if current_sorted is None:
                    lista_ordenada["last"] = new_node
       
        current = current["next"]

    return lista_ordenada

def selection_sort(my_list, sort_crit):
    
    if my_list["size"] <= 1:
        return my_list
    
    current = my_list["first"]
    menor = my_list["first"]["info"]
    
    
    while current != None:
        #RETORNA TRUE SI ELEMENT1 DEBE IR ANTES DEL 2
        menor = current
        next_node = current["next"]
        while next_node is not None:
            if sort_crit(next_node["info"], menor["info"]):  # Si next_node es menor que menor
                menor = next_node
            next_node = next_node["next"]
            
            if menor != current:
                current["info"], menor["info"] = menor["info"], current["info"]

        current = current["next"]

    return my_list

def shell_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list
    h = my_list["size"] // 3
    
    while h > 0:
        for i in range(h, my_list["size"]):
            current = get_element(my_list, i)
            valor = current

            j = i
            while j >= h:
                prev_node = get_element(my_list, j - h)

                if sort_crit(valor, prev_node) == True:
                    break  

                current = prev_node
                j -= h
                
          
            current = valor

        h = h // 3

    return my_list
#PRUEBAS
"""
sort_crit = default_sort_criteria
lista = new_list()
lista = add_last(lista, 3)
lista = add_last(lista, 2)
lista = add_last(lista, 1)
print(insertion_sort(lista, sort_crit))     
print(selection_sort(lista, sort_crit))    
print(shell_sort(lista, sort_crit))    
"""

def merge_sort(my_list, sort_crit):
    if size(my_list) > 1:
        mitad_izq = new_list() # Crea lista izq
        mitad_der = new_list() # Crea lista der
        for i in range(size(my_list)//2): # inserta a list izq
            add_last(mitad_izq, get_element(my_list, i))
        for j in range((size(my_list)//2)+1, size(my_list)): # inserta a list der
            add_last(mitad_der, get_element(my_list, j))
        merge_sort(mitad_izq, sort_crit)
        merge_sort(mitad_der, sort_crit)
        # Implementar el merge
        a = b = c = 0
        while a < size(mitad_izq) and b < size(mitad_der):
            if sort_crit(get_element(mitad_izq, a), get_element(mitad_der, b)):
                change_info(my_list, c, get_element(mitad_izq, a))
                a+=1
            else:
                change_info(my_list, c, get_element(mitad_der, b))
                b+=1
            c+=1
        while a < size(mitad_izq):
            change_info(my_list, c, get_element(mitad_izq, a))
            a +=1
            c += 1
        while b < size(mitad_der):
            change_info(my_list, c, get_element(mitad_der, b))
            b += 1
            c += 1
    return my_list

def quick_sort(my_list, sort_crit, low_index = 0, high_index = -1):
    if size(my_list)>1:
        if high_index == -1:
            high_index = size(my_list)-1 # indice del ultimo elemento en la lista para la primera llamada.
        pivote = get_element(my_list, high_index)
        seg = -1
        for curr in range(low_index, high_index):
            if sort_crit(get_element(my_list, curr), pivote):
                if (seg ==-1):
                    seg = curr
                else:
                    temp = get_element(my_list, seg)
                    change_info(my_list, seg, get_element(my_list, curr))
                    change_info(my_list, curr, temp)
                    seg +=1
        if seg != -1:
            temp = get_element(my_list, seg)
            change_info(my_list, seg, pivote)
            change_info(my_list, high_index, temp)
            quick_sort(my_list, sort_crit, low_index, seg -1)
            quick_sort(my_list, sort_crit, seg, high_index)

    return my_list