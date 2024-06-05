import ctypes

class Array :
    def __init__(self, size):
        assert size > 0
        self._size = size
        PyArraytype = ctypes.py_object * size
        self._elements = PyArraytype()
        self.clear(None)

    def __len__(self):
        return self._size
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self)
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
    def __iter__(self):
        return _ArrayItelator(self._elements)

class _ArrayItelator :
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopAsyncIteration
