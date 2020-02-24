class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = None
        # sell = 0
        max_profit = 0
        if len(prices) <= 1:
            return 0
        
        for i in range(len(prices)):
            p = prices[i]
            if buy is not None:
                if p < buy:
                    buy = p
                
                elif (p - buy > max_profit):
                    max_profit = p - buy
            else:
                buy = p
        return max_profit