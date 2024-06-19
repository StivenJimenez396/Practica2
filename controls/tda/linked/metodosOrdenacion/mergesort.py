class Mergesort:
    def sort_ascendent(self, array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.sort_ascendent(array[:mid])
        right = self.sort_ascendent(array[mid:])
        return self.merge_ascendent(left, right)

    def merge_ascendent(self, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

    def sort_descendent(self, array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.sort_descendent(array[:mid])
        right = self.sort_descendent(array[mid:])
        return self.merge_descendent(left, right)

    def merge_descendent(self, left, right):
        result = []
        while left and right:
            if left[0] >= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

    def sort_models_ascendent(self, array, attribute):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.sort_models_ascendent(array[:mid], attribute)
        right = self.sort_models_ascendent(array[mid:], attribute)
        return self.merge_models_ascendent(left, right, attribute)

    def merge_models_ascendent(self, left, right, attribute):
        result = []
        while left and right:
            if getattr(left[0], attribute) <= getattr(right[0], attribute):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

    def sort_models_descendent(self, array, attribute):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.sort_models_descendent(array[:mid], attribute)
        right = self.sort_models_descendent(array[mid:], attribute)
        return self.merge_models_descendent(left, right, attribute)

    def merge_models_descendent(self, left, right, attribute):
        result = []
        while left and right:
            if getattr(left[0], attribute) >= getattr(right[0], attribute):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result
