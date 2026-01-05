
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for  index ,val in enumerate(nums) :
            req = target - val 
            if req in d :
                return [index , d[req]]
            d[val] = index
        return [-1,-1]

        