[575745]
[575745]


class FreqStack:

    def __init__(self):
        self.groups = defaultdict(list)
        self.counts = defaultdict(int)
        self.top_group = 1
    def push(self, val: int) -> None:
        self.counts[val]+= 1
        group = self.counts[val]
        self.groups[group].append(val)
        if self.counts[val]> self.top_group:
            self.top_group = self.counts[val]

    def pop(self) -> int:
        res = self.groups[self.top_group].pop()
        self.counts[res]-= 1
        if not len(self.groups[self.top_group]):
            self.top_group-= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()