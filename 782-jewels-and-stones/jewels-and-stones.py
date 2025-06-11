class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        stones_dict =dict()
        output = 0 
        for stone in stones:
            if stone in stones_dict:
                stones_dict[stone]+=1
            else:
                stones_dict[stone]=1
        
        for jewel in jewels:
            if jewel in stones_dict:
                output+=stones_dict[jewel]
        return output