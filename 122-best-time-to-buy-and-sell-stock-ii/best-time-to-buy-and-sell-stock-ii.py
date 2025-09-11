class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        count = 0
        for i in range(0,n-1):
            if prices[i]<prices[i+1]:
                x = prices[i+1]-prices[i]
                count = x + count
        return count
                    
                




        
        