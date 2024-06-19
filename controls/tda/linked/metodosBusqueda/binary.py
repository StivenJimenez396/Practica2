from controls.tda.linked.metodosOrdenacion.quicksort import Quicksort

class Binary:
    def search_binary(self, array, element):
        quickSort = Quicksort()
        array = quickSort.sort_ascendent(array)  # Orden ascendente
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2  
            if array[middle] == element:
                return middle  
            elif array[middle] < element:
                left = middle + 1  
            else:
                right = middle - 1 
                
        return -1

    def search_binary_models(self, array, element, attribute):
        quickSort = Quicksort()
        array = quickSort.sort_models_descendent(array, attribute)  # Orden descendente por atributo
        element = str(element).upper()  # Convertir element a cadena y hacer mayúsculas
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2
            middle_value = str(getattr(array[middle], attribute)).upper()  # Obtener el valor del atributo como cadena y hacer mayúsculas
            if middle_value == element:
                return middle
            elif middle_value < element:
                left = middle + 1
            else:
                right = middle - 1
        return -1