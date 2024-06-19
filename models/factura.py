from models.persona import Persona
class Factura(Persona):
    def __init__(self):
        super().__init__()
        self.__valor = 0.0
        self.__numFactura = ""
        self.__dniEmisor = ""
        self.__valorTotal = 0.0
        self.__porcentajeRetencion = 0.0
        self.__retencion = 0.0

    @property
    def _porcentajeRetencion(self):
        return self.__porcentajeRetencion

    @_porcentajeRetencion.setter
    def _porcentajeRetencion(self, value):
        self.__porcentajeRetencion = value

    @property
    def _retencion(self):
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value

    @property
    def _valorTotal(self):
        return self.__valorTotal

    @_valorTotal.setter
    def _valorTotal(self, value):
        self.__valorTotal = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _numFactura(self):
        return self.__numFactura

    @_numFactura.setter
    def _numFactura(self, value):
        self.__numFactura = value

    @property
    def _dniEmisor(self):
        return self.__dniEmisor

    @_dniEmisor.setter
    def _dniEmisor(self, value):
        self.__dniEmisor = value


    @property
    def serializable(self):
        data = super().serializable
        data.update({
            "valor": self.__valor,
            "numFactura": self.__numFactura,
            "dniEmisor": self.__dniEmisor,
            "valorTotal": self.__valorTotal,
            "porcentajeRetencion": self.__porcentajeRetencion,
            "retencion": self.__retencion,
        })
        return data
    
    def deserializar(data):
        factura = Factura()
        factura._id = data["id"]
        factura._nombre = data["nombre"]
        factura._apellido = data["apellido"]
        factura._cedula = data["cedula"]
        factura._tipoRuc = data["tipoRuc"]
        factura._numRuc = data["numRuc"]
        factura._valor = data["valor"]
        factura._numFactura = data["numFactura"]
        factura._dniEmisor = data["dniEmisor"]
        factura._valorTotal = data["valorTotal"]
        factura._porcentajeRetencion = data["porcentajeRetencion"]
        factura._retencion = data["retencion"]
        return factura