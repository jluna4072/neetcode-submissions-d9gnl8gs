class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = float("-inf")
        bought = prices[0]
        for p in prices:
            if p < bought:
                bought = p
            profit = p - bought
            mx = max(mx, profit)

        return mx
            