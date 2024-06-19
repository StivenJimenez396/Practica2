from controls.dao.daoAdapter import DaoAdapter
from controls.tda.linked.linkedList import Linked_List
from models.persona import Persona

class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Persona)
        self.__persona = None
        

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value
        
    
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._persona._id = self._lista._length + 1
        self._save(self._persona)
        
    
    def merge(self,pos):
        self._merge(self._persona, pos)
        
    def sort_lista(self, attribute, order, metodo):
        type_order = 1 if order == 'asc' else 2
        return self.sort(attribute, type_order, metodo)
    
