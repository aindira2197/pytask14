class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.order.remove(key)
            self.order.append(key)
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self.order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value
            self.order.append(key)

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            self.order.remove(key)

    def display(self):
        print(self.cache)

class LRUCacheDict:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def __getitem__(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.order.remove(key)
            self.order.append(key)
            return value
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self.order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value
            self.order.append(key)

    def __delitem__(self, key):
        if key in self.cache:
            del self.cache[key]
            self.order.remove(key)

    def __contains__(self, key):
        return key in self.cache

    def display(self):
        print(self.cache)

def main():
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    print(cache.get(1))
    cache.put(4, 4)
    print(cache.get(2))
    cache.delete(1)
    print(cache.get(1))
    cache.display()

    cache_dict = LRUCacheDict(3)
    cache_dict[1] = 1
    cache_dict[2] = 2
    cache_dict[3] = 3
    print(cache_dict[1])
    cache_dict[4] = 4
    print(2 in cache_dict)
    del cache_dict[1]
    print(1 in cache_dict)
    cache_dict.display()

if __name__ == "__main__":
    main()