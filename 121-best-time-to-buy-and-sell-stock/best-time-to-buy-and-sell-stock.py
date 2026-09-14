class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowset_price = prices[0]
        hightest_price = prices[0]
        max_profit = 0
        if prices[1:]:
            for num in prices[1:]:
                if num < lowset_price:
                    lowset_price=num
                    hightest_price = num
                else:
                    hightest_price = num
                    max_profit = max(max_profit,hightest_price-lowset_price)
        else:
            return max_profit
        return max_profit


        