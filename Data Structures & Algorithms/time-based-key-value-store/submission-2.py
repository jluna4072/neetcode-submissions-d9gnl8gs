class TimeMap:

    def __init__(self):
        self.keys_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys_map[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if not self.keys_map[key] or self.keys_map[key][0][0] > timestamp:
            return ""
        l, r = 0, len(self.keys_map[key]) - 1
        while l<=r:
            m = (l + r)// 2
            if self.keys_map[key][m][0] == timestamp:
                return self.keys_map[key][m][1] 
            elif self.keys_map[key][m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return self.keys_map[key][r][1]
        
