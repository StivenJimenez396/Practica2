class Shellsort:
    def sort_ascendent(self, array):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array

    def sort_descendent(self, array):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] < temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array

    def sort_models_ascendent(self, array, attribute):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and getattr(array[j - gap], attribute) > getattr(temp, attribute):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array

    def sort_models_descendent(self, array, attribute):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and getattr(array[j - gap], attribute) < getattr(temp, attribute):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array
