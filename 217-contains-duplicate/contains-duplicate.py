class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}

        for num in nums:
            # d.get fucntion will appends the element if is not there in dictionary 
            d[num]=d.get(num,0)+1
            if d[num]>1:
                return True
        return False 
        