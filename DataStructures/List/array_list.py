def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    #lista.insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

#print(add_last(lista, 6))
#print(add_last(lista, 7))

def size(my_list):
    return my_list["size"]
#print(size(lista))

def first_element(my_list):
    lista = my_list["elements"]
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    else:
        return lista[0]
    
#print(first_element(lista))

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    
    else:
        return False
#print(is_empty(lista))

def last_element(my_list):
    lista = my_list["elements"]
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    else:
        return lista[-1]
    
#print(last_element(lista))

def delete_element(my_list, pos):
    if 0 <= pos < my_list["size"]:
        del my_list["elements"][pos]
        my_list["size"] -= 1
        return my_list
    else:
        raise Exception("IndexError: list index out of range")

#print(delete_element(lista, 1))

def remove_first(my_list):
    if my_list["size"] > 0:
        primero =  my_list["elements"][0]
        del my_list["elements"][0]
        my_list["size"] -= 1
        return primero
    else:
        raise Exception("IndexError: list index out of range")
    
#print("remove first",remove_first(lista))

def remove_last(my_list):
    if my_list["size"] > 0:
        ultimo =  my_list["elements"][my_list["size"] -1]
        del my_list["elements"][my_list["size"] -1]
        my_list["size"] -= 1
        return ultimo
    else:
        raise Exception("IndexError: list index out of range")
#print("remove last",remove_last(lista))   

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

#print(insert_element(lista, 8, 1))

def change_info(my_list, pos, new_info):
    if 0 <= pos < my_list["size"]:
        my_list["elements"][pos] = new_info
        #del my_list["elements"][pos]
        #my_list["elements"].insert(pos, new_info)
        return my_list
    else:
        raise Exception("IndexError: list index out of range")

#print(change_info(lista, 1, 2))

def exchange(my_list, pos_1, pos_2):
    if 0 <= pos_1 < my_list["size"] and  0 <= pos_2 < my_list["size"]:
        e_1 = my_list["elements"][pos_1]
        my_list["elements"][pos_1] = my_list["elements"][pos_2]
        
        my_list["elements"][pos_2] = e_1
        return my_list
    else:
        raise Exception("IndexError: list index out of range")
#print("exchange",exchange(lista, 1, 2))


def sub_list(my_list, pos_i, num_elements):
    if 0 <= pos_i < my_list["size"]:
        sub_lista = my_list["elements"][pos_i:pos_i + num_elements]
        array_sub_lista =  {
        'elements': sub_lista,
        'size': len(sub_lista),
        }   
        return array_sub_lista
    else:
        raise Exception("IndexError: list index out of range")
#print(sub_list(lista, 1, 2))

# Funciones Laboratorio 5: Algoritmos de ordenamiento iterativo

def default_sort_criteria(element_1, element_2):
   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted
#lista = new_list()
#print(add_first(lista, 4))
#print(add_first(lista, 3))

def selection_sort (my_list, sort_crit):
    if my_list['size'] <= 1:
        return my_list
    else:
        for i in range(0,my_list['size']):
            menor_pos = i
            comparacion = i + 1
            while comparacion < my_list['size']:
                if not sort_crit(my_list['elements'][menor_pos],my_list['elements'][comparacion]):
                    menor_pos = comparacion
                comparacion += 1
            exchange(my_list,i,menor_pos)
    return my_list

def insertion_sort (my_list, sort_crit):
    size = my_list["size"]
 
    for i in range (1,size):
         elem_actual = my_list["elements"][i]
         pos = i -1
         
         while pos >= 0 and sort_crit(elem_actual, my_list["elements"][pos]):
             my_list["elements"][pos + 1] = my_list["elements"][pos]
             pos -= 1
         
         my_list["elements"][pos + 1] = elem_actual
         
    return my_list

def shell_sort(my_list,sort_crit):
    size = my_list["size"]
    h = size // 3 

    while h > 0:
        for i in range(h, size):
            temp = my_list["elements"][i]  
            j = i

            while j >= h and not sort_crit(my_list["elements"][j - h], temp):
                my_list["elements"][j] = my_list["elements"][j - h]
                j -= h

            my_list["elements"][j] = temp  
        
        h = h // 3  

    return my_list
    
    
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

#lista = new_list()
#sort_crit = default_sort_criteria
#print(add_first(lista, 4))
#print(add_first(lista, 3))
#print(add_first(lista, 7))
#print(add_first(lista, 9))
#print(add_first(lista, 15))
#print(add_first(lista, 2))
#print(insertion_sort(lista, sort_crit))