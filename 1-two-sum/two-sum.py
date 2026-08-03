from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = defaultdict(int)
        for dictIndex in range(len(nums)):
            need = target - nums[dictIndex]
            if need in dictt:
                return [dictt[need] , dictIndex]
            else :
                dictt[nums[dictIndex]] =dictIndex
        return [-1,-1]
            
        