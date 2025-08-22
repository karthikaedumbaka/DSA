class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # by using Sliding window
        l,r=0,1
        profit=0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return profit

        # time O(n)
        # space O(1)
