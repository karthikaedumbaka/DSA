class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''# BF 
        # i will use 2 for loop , first loop for pick the numbder and 
        #second loop for to chek it is repeating or not 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False 
        # time 0(n^2)
        # space  0(1)'''
        '''
        # but on optimal solution we can use the dictionary 
        d={}
        for i in nums:
            d[i] = d.get(i,0)+1
            if d[i] > 1:
                return True
        return False '''

        s =set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False        