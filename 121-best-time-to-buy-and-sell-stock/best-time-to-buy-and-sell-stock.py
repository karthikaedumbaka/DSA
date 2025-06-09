class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_number=float("inf")
        for p in prices:
            if p < min_number:
                min_number = p
            elif p-min_number> max_profit:
                max_profit=p-min_number

        return max_profit
        # time O(n)
        # space O(1)
        