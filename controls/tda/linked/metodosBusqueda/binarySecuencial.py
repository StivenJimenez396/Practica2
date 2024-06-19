from controls.tda.linked.metodosBusqueda.binary import Binary
from controls.tda.linked.metodosBusqueda.secuencial import Secuencial
from controls.tda.linked.metodosOrdenacion.quicksort import Quicksort

class BinarySecuencial:
    def search_BinarySecuencial(self, array, element):
        quickSort = Quicksort()
        binary = Binary()
        secuencial = Secuencial()

        sorted_array = quickSort.sort_ascendent(array)  # Orden ascendente usando Quicksort
        index = binary.search_binary(sorted_array, element)  # Búsqueda binaria en el array ordenado
        if index == -1:
            return -1
        
        return secuencial.search_sequential_primitive(sorted_array, element)  # Búsqueda secuencial del elemento

    def search_BinarySecuencial_models(self, array, element, attribute):
        quickSort = Quicksort()
        binary = Binary()
        secuencial = Secuencial()

        sorted_array = quickSort.sort_models_descendent(array, attribute)  # Orden descendente por atributo usando Quicksort
        index = binary.search_binary_models(array, element, attribute)  # Búsqueda binaria en el array de modelos ordenado
        if index == -1:
            return -1
        
        return secuencial.search_sequential_models(array, element, attribute, index)  # Búsqueda secuencial de modelos
