from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        stones_dict= Counter(stones)
        jewels_set= set(jewels)
        for stone , val in stones_dict.items():
            if stone in jewels_set:
                count += val
        return count