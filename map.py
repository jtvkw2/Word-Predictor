class Map:
    def __init__(self):
        self.hash_table = [[] for _ in range(10)]
        self.count = 0

    def hashing_function(self, key):
        return hash(key) % len(self.hash_table)

    def insert(self, key, value):
        hash_key = self.hashing_function(key)
        key_exists = False
        bucket = self.hash_table[hash_key]
        current_val = 0
        i = 0
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                current_val = v
                break
        if key_exists:
            if type(current_val) is int:
                bucket[i] = (key, current_val + 1)
            else:
                bucket[i] = [key, current_val]
        else:
            bucket.append((key, value))
            self.count += 1

    def get(self, key):
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v
        return 0
