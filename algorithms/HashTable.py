class HashTable:
    def __init__(self, size=1_000) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for tkey, tvalue in self.table[index]:
            if tkey == key:
                self.table[index].remove((tkey, value))
                break
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for tkey, tvalue in self.table[index]:
            if tkey == key:
                return tvalue
        return None


hash_table = HashTable()
hash_table.set("name", "Autumn")
hash_table.set("city", "London")

print(hash_table.get("name"))
print(hash_table.get("city"))
print(hash_table.get("phone"))
