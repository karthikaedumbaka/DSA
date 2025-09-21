from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # stones_dict =dict()
        # output = 0 
        # for stone in stones:
        #     if stone in stones_dict:
        #         stones_dict[stone]+=1
        #     else:
        #         stones_dict[stone]=1
        
        # for jewel in jewels:
        #     if jewel in stones_dict:
        #         output+=stones_dict[jewel]
        # return output
        stones_dict = Counter(stones)
        jewels_set=set(jewels)
        ans=0
        for stone,freq in stones_dict.items():
            if stone in jewels_set:
                ans+=freq
        return ans

# Time Complexity: O(n + m)

# Space Complexity: O(m + u) ≈ O(m)