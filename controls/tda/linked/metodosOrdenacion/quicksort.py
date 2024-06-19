class Quicksort:
    def sort_ascendent(self, array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return self.sort_ascendent(less) + [pivot] + self.sort_ascendent(greater)

    def sort_descendent(self, array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        less = [x for x in array[1:] if x >= pivot]
        greater = [x for x in array[1:] if x < pivot]
        return self.sort_descendent(less) + [pivot] + self.sort_descendent(greater)

    def sort_models_ascendent(self, array, attribute):
        if len(array) <= 1:
            return array
        pivot = array[0]
        less = [x for x in array[1:] if getattr(x, attribute) <= getattr(pivot, attribute)]
        greater = [x for x in array[1:] if getattr(x, attribute) > getattr(pivot, attribute)]
        return self.sort_models_ascendent(less, attribute) + [pivot] + self.sort_models_ascendent(greater, attribute)

    def sort_models_descendent(self, array, attribute):
        if len(array) <= 1:
            return array
        pivot = array[0]
        less = [x for x in array[1:] if getattr(x, attribute) >= getattr(pivot, attribute)]
        greater = [x for x in array[1:] if getattr(x, attribute) < getattr(pivot, attribute)]
        return self.sort_models_descendent(less, attribute) + [pivot] + self.sort_models_descendent(greater, attribute)
