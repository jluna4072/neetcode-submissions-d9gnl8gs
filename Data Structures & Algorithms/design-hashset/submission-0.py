class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(1001)]

    def add(self, key: int) -> None:
        bucket = key % 1001
        if not self.contains(key):
            self.buckets[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % 1001
        n = len(self.buckets[bucket])
        for i,k in enumerate(self.buckets[bucket]):
            if key == k:
                self.buckets[bucket][i], self.buckets[bucket][n - 1] = self.buckets[bucket][n - 1], self.buckets[bucket][i] 
                self.buckets[bucket].pop()
                return
        return
    def contains(self, key: int) -> bool:
        bucket = key % 1001
        for k in self.buckets[bucket]:
            if key == k:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)