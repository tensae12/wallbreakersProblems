class LRUCache:

    def __init__(self, capacity: int):
        self.obj = collections.OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.obj:
            return -1
        else:
            value = self.obj[key]
            self.obj.move_to_end(key)
            return value


    def put(self, key: int, value: int) -> None:
        if key in self.obj:
            obj.pop(key)

        self.obj[key] = value
        if self.capacity < len(self.obj):
            oldest = next(iter(self.obj))
            del self.obj[oldest]