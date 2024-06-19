from typing import TypeVar, Generic
from controls.tda.linked.linkedList import Linked_List
import os.path
import json
import os

T = TypeVar('T')

class DaoAdapter(Generic[T]):
    atype: T

    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/data/"
    
    def _list(self) -> T:
        if os.path.isfile(self.URL+self.file):
            with open(self.URL+self.file, "r") as f:
                datos = json.load(f)
                self.lista.clear
                for data in datos:
                    a = self.atype.deserializar(data)
                    self.lista.add(a, self.lista._length)
        return self.lista
    
    def __tranform__(self):
        aux = "["
        for i in range(0, self.lista._length):
            if i < self.lista._length - 1:
                aux += str(json.dumps(self.lista.get(i).serializable))+","
            else:
                aux += str(json.dumps(self.lista.get(i).serializable))
        aux += "]"
        return aux
    
    def to_dic_lista(self, lista):
        aux = []
        for i in range(0, lista._length):
            aux.append(lista.get(i).serializable)
        return aux
    
    def to_dic(self):
        aux = []
        lista = self._list()
        for i in range(0, lista._length):
            aux.append(lista.get(i).serializable)
        return aux
    
    
    def _get(self, id):
        list = self.list()
        array = list.toArray
        for i in range(0, len(array)):
            if array[i]._id == id:
                return array[i]
        return None
            
    def _save(self, data: T):
        self._list()
        self.lista.add(data, self.lista._length)
        with open(self.URL+self.file, "w") as a:
            a.write(self.__tranform__())
        
    def _merge(self, data: T, pos):
        self._list()
        self.lista.edit(data, pos)
        with open(self.URL+self.file, "w") as a:
            a.write(self.__tranform__())
    
    def _delete(self, pos):
        self._list()
        self.lista.remove(pos)
        with open(self.URL+self.file, "w") as a:
            a.write(self.__tranform__())
        

