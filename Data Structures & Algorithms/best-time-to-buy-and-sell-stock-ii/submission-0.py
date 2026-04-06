class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Greedy
        We buy a stock every day, and if teh next day is greater than it, we sell. If its less, 
        we can act like we sold it the same day, so we dont lose money

        '''

        bought = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            cur = prices[i]
            if cur > bought:
                profit+= (cur - bought)
            bought = cur
        
        return profit


