import sys
class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        id = sys.getsizeof(key)
        for i in range(self.size):
            if self.slots[i] is not None:
                idx_of_slot = sys.getsizeof(self.slots[i])
                id =  id + idx_of_slot
        id = id % self.size
        return id

    def is_key(self, key):
        if key in self.values:
            return True
        else:
            return False
         # возвращает True если ключ имеется,
         # иначе False
    def put(self, key, value):
        if key in self.values:
            for i in range(self.size):
                if self.values[i] == key:
                    self.slots[i] = value
                    break
        else:
            id_key = self.hash_fun(key)
            if self.values[id_key] is not None:
                for i in range(1,self.size):
                    id_key = id_key + (i * self.hash_fun(key))
                    id_key = id_key % self.size
                    if self.values[id_key] is None:
                        break
            if self.values[id_key] is not None:
                for i in range(self.size):
                    if self.values[i] is None:
                        id_key = i
                        break
            self.values[id_key] = key
            self.slots[id_key] = value

    def get(self, key):
        if self.is_key(key) is True:
            for i in range(self.size):
                if self.values[i] == key:
                    return self.slots[i]
        else:
            return None
         # возвращает value для key, 
         # или None если ключ не найден
