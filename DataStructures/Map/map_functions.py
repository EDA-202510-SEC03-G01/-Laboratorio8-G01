import math
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me

#from ..List import array_list as lt
#import map_entry as me
"""
    Funciones auxiliares para el manejo de tablas de simbolos (**mapas**)
"""


def is_prime(n):
    """Valida si un número es primo o no

    :param n: Número a validar
    :type n: int

    :return: True si es primo, False en caso contrario
    """
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def next_prime(n):
    """
    Encuentra el siguiente número primo mayor a n

    :param n: Número a partir del cual se busca el siguiente primo
    :type n: int

    :return: El siguiente número primo mayor a n
    """
    found = False
    next_p = 1
    # Base case
    if n <= 1:
        next_p = 2
        found = True
    if found is False:
        next_p = int(n)
        # Loop continuously until is_prime returns
        # True for a number greater than n
        while not found:
            next_p = next_p + 1
            if is_prime(next_p):
                found = True
    return int(next_p)


def hash_value(table, key):
    """
    Calcula un hash para una llave, utilizando el método
    MAD : hash_value(y) = ((a*y + b) % p) % M.

    Donde:
    M es el tamaño de la tabla, primo
    p es un primo mayor a M,
    a y b enteros aleatoreos dentro del intervalo [0,p-1], con a > 0

    :param table: Tabla de hash
    :type table: map
    :param key: Llave a la que se le calculará el hash
    :type key: any

    :return: Valor del hash
    :rtype int
    """

    h = hash(key)
    a = table["scale"]
    b = table["shift"]
    p = table["prime"]
    m = table["capacity"]

    value = int((abs(a * h + b) % p) % m)
    return value

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1