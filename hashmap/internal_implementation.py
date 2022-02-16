
# print(get_hash('march 6'))


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None] * self.MAX

    def get_hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
 

h = HashTable()
h['march 6'] = 302
h['march 11'] = 78
h['march 6']
# print(h.arr)
print(h['march 11'])
