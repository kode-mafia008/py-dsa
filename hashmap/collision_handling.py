class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if(len(element) == 2 and element[0] == key):
                self.arr[h][index] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0 == key]:
                return kv[1]

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                del self.arr[arr_index][index]


t = HashTable()
t.get_hash('march 6')

# print(t.get_hash('march 6'))
# print(t.get_hash('march 17'))

t['march 6'] = 120
t['march 6'] = 45
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

# print(t['march 6'])

#updating 
# print(t.arr)
# t['march 17'] = 420

#deleting 
print(t.arr)
del t['march 17']
print(t.arr)
