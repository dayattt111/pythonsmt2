class PQbase:
    class _item:
        __slot__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def         