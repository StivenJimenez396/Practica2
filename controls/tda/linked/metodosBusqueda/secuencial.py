class Secuencial:
    def search_sequential_primitive(self, array, element):
        for i in range(len(array)):
            if array[i] == element:
                return i
        return -1

    def search_sequential(self, array, element, index):
        left = index
        right = index
        while left > 0 and array[left - 1] == element:
            left -= 1
        while right < len(array) - 1 and array[right + 1] == element:
            right += 1
       
        return array[left:right + 1]

    def search_sequential_models(self, array, element, attribute, index):
        element = element.upper()
        left = index
        right = index
        while left > 0 and getattr(array[left - 1], attribute).upper() == element:
            left -= 1
        while right < len(array) - 1 and getattr(array[right + 1], attribute).upper() == element:
            right += 1
        return array[left:right + 1]
