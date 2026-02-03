from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d= defaultdict(int)
        for index,value in enumerate(nums):
            req = target - value
            if req in d:
                return [d[req],index]
            d[value] = index
        return [-1,-1]

        