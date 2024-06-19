import sys
sys.path.append('../')

from controls.tda.linked.linkedList import Linked_List
from controls.personaDaoControl import PersonaDaoControl
from controls.tda.linked.metodosBusqueda.binary import Binary
import random
import time

pdc = PersonaDaoControl()
try:
    lista = Linked_List()
    for i in range(100):
        lista.add(round(random.random()*10))

    print("Tiempo de quicksort")
    inicio = time.time()
    lista.sort(type=1, metodo="quicksort")
    fin = time.time()
    print("Tiempo de ejecución: "+str(fin-inicio))
    
    inicio = time.time()
    lista.search_binary(10)
    fin = time.time()
    print("Tiempo de ejecución: "+str(fin-inicio))   
    
    inicio = time.time()
    lista.search_binarySecuencial(10)
    fin = time.time()
    print("Tiempo de ejecución: "+str(fin-inicio))   
    
#    print("Tiempo de quicksort")    
#    inicio = time.time()
#    lista.sort(type=2, metodo="quicksort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de mergesort") 
#    inicio = time.time()
#    lista.sort(type=1, metodo="mergesort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de mergesort") 
#    inicio = time.time()
#    lista.sort(type=2, metodo="mergesort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de shellsort") 
#    inicio = time.time()
#    lista.sort(type=1, metodo="shellsort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))
    
#    print("Tiempo de shellsort") 
#    inicio = time.time()
#    lista.sort(type=2, metodo="shellsort")
#    fin = time.time()
#    print("Tiempo de ejecución: "+str(fin-inicio))

except Exception as error:
    print("Errores")
    print(error)
    