class MyHashMap:

    def __init__(self):
        self.keys = [False] * 1000001
        self.values = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.keys[key] = True
        self.values[key] = value

    def get(self, key: int) -> int:
        return self.values[key] if self.keys[key] else -1

    def remove(self, key: int) -> None:
        self.keys[key] = False
        self.values[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)