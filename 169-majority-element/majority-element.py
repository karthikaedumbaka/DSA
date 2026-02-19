from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_value = (len(nums)//2)+1
        count_num = defaultdict(int)

        for num in nums:
            count_num[num] +=1
            if count_num[num] >= majority_value:
                return num
        return [-1,-1]

        