from controls.tda.linked.node import Node
from controls.exception.linkedEmpty import LinkedEmpty
from controls.exception.arrayPositionException import ArrayPositionException
from numbers import Number
from controls.tda.linked.burbuja import Burbuja
from controls.tda.linked.insercion import Insercion
from controls.tda.linked.metodosOrdenacion.mergesort import Mergesort
from controls.tda.linked.metodosOrdenacion.quicksort import Quicksort
from controls.tda.linked.metodosOrdenacion.shellsort import Shellsort
from controls.tda.linked.metodosBusqueda.binary import Binary
from controls.tda.linked.metodosBusqueda.binarySecuencial import BinarySecuencial
from controls.tda.linked.metodosBusqueda.secuencial import Secuencial

class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node            
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
        
        self.__length += 1

    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)            
        else:            
            node = Node(data)
            self.__last._next = node
            self.__last = node        
            self.__length += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:            
            self.__addLast__(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next#self.getNode(pos) 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:            
            self.__last._data = data
        else:                        
            node = self.getNode(pos)            
            node._data = data
            '''
    @property
    def toArray(self):
        array = TDAArray(self._length)
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while node < self.__length:
                array.insert(node._data,cont)
                cont += 1
                node = node._next
        return array'''
                   
        
    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            #self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element

    
    def delete(self, pos = 0):
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position out range")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == (self.__length - 1):
            return self.deleteLast()
        else:
            preview = self.getNode(pos - 1)
            actually = self.getNode(pos)
            element = preview._data
            next = actually._next
            actually = None
            preview._next = next
            self._length = self._length - 1
            return element

    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    """Obtiene el objeto nodo"""
    def get(self, pos):
        try:
            return self.getNode(pos)._data
        except Exception as error:
            return None
        
            
    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out
    
    
    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)
        
    @property
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._length:
                array.append(node._data)
                cont += 1
                node = node._next
        return array
    
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])      
    # a < b
    
    
    def sort(self, type, metodo="insercion"):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if metodo == "quicksort":
                sorter = Quicksort()
                if type == 1:
                    array = sorter.sort_ascendent(array)
                else:
                    array = sorter.sort_descendent(array)
            elif metodo == "mergesort":
                sorter = Mergesort()
                if type == 1:
                    array = sorter.sort_ascendent(array)
                else:
                    array = sorter.sort_descendent(array)
            elif metodo == "shellsort":
                sorter = Shellsort()
                if type == 1:
                    array = sorter.sort_ascendent(array)
                else:
                    array = sorter.sort_descendent(array)
            else:

                order = Insercion()
                if type == 1:
                    array = order.sort_primitive_ascendent(array)
                else:
                    array = order.sort_primitive_descendent(array)

            self.toList(array)             
   
    def sort_models(self, attribute, tipo=1, metodo=""):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if metodo == "quicksort":
                sorter = Quicksort()
            elif metodo == "mergesort":
                sorter = Mergesort()
            elif metodo == "shellsort":
                sorter = Shellsort()
            else:
                raise ValueError("Método de ordenación no soportado")

            if tipo == 1:
                array = sorter.sort_models_ascendent(array, attribute)
            else:
                array = sorter.sort_models_descendent(array, attribute)

            self.toList(array)
        return self
        
        
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            #print(len(array))
            for i in range(0, len(array)):
                #print(type (data))   
                if array[i].lower().__contains__(data.lower()):#tartswith(data.lower())):
                    list.add(array[i], list._length)
        return list
    
    def search_binary(self, element):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            search = Binary()
            index = search.search_binary(array, element)
            if index == -1:
                print(f"Elemento {element} no encontrado")
            else:
                print(f"Elemento {element} encontrado en el índice: {index}")
            
        self.toList(array)
        return self

    def search_binary_models(self, element, attribute):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            
            search = Binary()
            quickSort = Quicksort()
            array = quickSort.sort_models_descendent(array, attribute)
            index = search.search_binary_models(array, element, attribute)
            
            if index == -1:
                print(f"Models con {attribute} = {element} no encontrado")
            else:
                print(f"Models con {attribute} = {element} encontrado en el objeto: {index}")
        
        self.toList(array)
        #return self
        return index
    
    
    def search_binarySecuencial(self, element):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            search = BinarySecuencial()
            index = search.search_BinarySecuencial(array, element)
            if index == -1:
                print(f"Elemento {element} no encontrado")
            else:
                print(f"Elemento {element} fue encontrado en estas ocasiones: {index}")
            
        self.toList(array)
        return self

    def search_binarySecuencial_models(self, element, attribute):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
                
            array = self.toArray
            search = BinarySecuencial()
           
            index = search.search_BinarySecuencial_models(array, element, attribute)
            #print(index)
            aux = []
            if index == -1:
                print(f"Models con {attribute} = {element} no encontrado")
            else:
                print(f"los modelos con {attribute} = {element} fueron encontrados en:") #{index}
                
                for i in range(0, len(index)):
                    aux.append(index[i].serialize)
        
        self.toList(aux)

'''    def sort_models(self,attribute, type = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                #order = Burbuja()
                #order = Insercion()
                #order = Quicksort()
                #order = Shellsort()
                order = Mergesort()
                if type == 1:
                    #array = order.sort_burbuja_attribute_ascendent(array, attribute)
                    array = order.sort_models_ascendent(array, attribute)
                else:
                    #array = order.sort_burbuja_attribute_descendent(array, attribute)
                    array = order.sort_models_descendent(array, attribute)
                #cls = getattr(array[0], attribute)
                #print(cls)
            self.toList(array)
        return self'''
        
    #def sort(self, type):
    #    if self.isEmpty:
    #        raise LinkedEmpty("List empty")
    #    else:
    #        array = self.toArray
    #        # Datos primitivos
    #        if isinstance(array[0], Number) or isinstance (array[0], str):
                #order = Burbuja()
    #            order = Insercion()
    #            if type == 1:
                    #array = order.sort_burbuja_number_ascendent(array)
    #                array = order.sort_primitive_ascendent(array)
    #            else:
    #                array = order.sort_primitive_descendent(array)
                    #array = order.sort_burbuja_number_descendent(array)
    #        self.toList(array)
    
    #def sort_models(self,attribute, type = 1):
    #    if self.isEmpty:
    #        raise LinkedEmpty("List empty")
    #    else:
    #        array = self.toArray
    #        if isinstance(array[0], object):
                #order = Burbuja()
    #            order = Insercion()
    #            if type == 1:
                    #array = order.sort_burbuja_attribute_ascendent(array, attribute)
    #                array = order.sort_models_ascendent(array, attribute)
    #            else:
                    #array = order.sort_burbuja_attribute_descendent(array, attribute)
    #                array = order.sort_models_descendent(array, attribute)
                #cls = getattr(array[0], attribute)
                #print(cls)
    #        self.toList(array)
    #    return self
    
