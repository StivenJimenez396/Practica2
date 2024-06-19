from models.factura import Factura
from controls.dao.daoAdapter import DaoAdapter

class FacturaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None

    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()
        return self.__factura

    @_factura.setter
    def _factura(self, value):
        self.__factura = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._factura._id = self._lista._length + 1
        self._save(self._factura)
         
    def merge(self,pos):
        self._merge(self._factura, pos)
        
    #Acciones que se debe realizar dependiendo del tipo de ruc Educativa 0.08 y la profecional el 0.1 por ciento de retenciones
    def calcularRetencion(self):
        tipo_ruc = self._factura._tipoRuc.lower()
        if tipo_ruc == 'educativo':
            self._factura._porcentajeRetencion = 0.08 
        elif tipo_ruc == 'profecional':
            self._factura._porcentajeRetencion = 0.10
        else:
            print("Error: Tipo de RUC no válido")
            self._factura._porcentajeRetencion = 0.0
        self._factura._retencion = self._factura._valor * self._factura._porcentajeRetencion
        return self._factura._retencion
    
    def totalPago(self):
        self.__factura._valorTotal = self.__factura._valor - self.__factura._retencion 
        return self.__factura._valorTotal