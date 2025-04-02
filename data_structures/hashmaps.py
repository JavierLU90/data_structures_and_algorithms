class HashMap:
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
    
    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)
    
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
        if self.current_load() < 0.05:
            return
        old_hashmap = self.hashmap
        self.hashmap = [None] * (len(old_hashmap) * 10)
        for kvp in old_hashmap:
            if kvp is not None:
                key, value = kvp
                index = self.key_to_index(key)
                self.hashmap[index] = (key, value)

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        count = 0
        for slot in self.hashmap:
            if slot is not None:
                count += 1
        return count / len(self.hashmap)

    def get(self, key):
        i = self.key_to_index(key)
        bucket = self.hashmap[i]
        if bucket is None:
            raise Exception("sorry, key not found")
        return bucket[1]
    
    '''
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")
    '''


'''
HASH MAPS

A hash map or "hash table" is a data structure that maps keys to values:
    "bob"       ->  "ross"
    "pablo"     ->  "picasso"
    "leonardo"  ->  "davinci"

The lookup, insertion, and deletion operations of a hashmap have an average computational cost of O(1). 
Assuming you know the key, nothing beats a hashmap! A Python dictionary is an example of a hashmap. 
See, you already know what a hashmap is!

Under the Hood

While hashmaps are simple to use 
- you're already proficient with them if you know how to use a Python dictionary - 
the implementation is a bit trickier.

Hashmaps are built on top of arrays (or in the case of ours, a Python list). 
They use a hash function to convert a "hashable" key into an index in the array. 
From a high-level, all that matters to us is that the hash function:
    Takes a key and returns an integer.
    Always returns the same integer for the same key.
    Always returns a valid index in the array (e.g. not negative, and not greater than the array size)

Ideally the hash function hashes each key to a unique index, 
but most hash table designs employ an imperfect hash function, 
which might cause hash collisions where the hash function generates the same index for more than one key. 
An example of a collision in the above example would be "bob" and "leonardo" both hashing to index 3. 
Ideally "leonardo" would hash to some other index, like 2.

Such collisions are typically accommodated for, and are not a problem in practice.
'''