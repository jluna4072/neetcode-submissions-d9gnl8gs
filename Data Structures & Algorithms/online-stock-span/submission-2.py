'''
85,
75,4
80, 1
100, 1


The stocks will be added to stack like: (stock, span), where the first element of the
tuple is the stock and the second is the span of that stock

1. Before we add stock to stack, we keep checking the top of stack. If its empty or
the top is > the stock, we add it to stack. 

While the top of stack is less than the cur stock, we add the span of the top to the cur stock.
'''

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cur_span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            cur_span+= prev_span
        self.stack.append((price, cur_span))
        return cur_span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)