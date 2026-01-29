from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #to store the visit values with idex as value 
        d=defaultdict(int)
        # we are using enumarate funtion to get the both index and value form the input 
        for  index,value in enumerate(nums):
            # we are check if our reqq is present in dicti or not 
            req = target - value
            # if it present and check the req index and currect index are not equal  then 
            if req in d  and d[req] != index:
                # we are return the output
                return [d[req] , index]
            # and the see vale with index to dictionary
            d[value] = index
        return [-1,-1]