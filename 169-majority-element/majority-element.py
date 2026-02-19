from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority_value = (len(nums)//2)+1
        # count_num = defaultdict(int)

        # for num in nums:
        #     count_num[num] +=1
        #     if count_num[num] >= majority_value:
        #         return num
        # return -1

        # Moore's Voting Algorithm

        majority_value = 0
        count = 0

        for num in nums:
            if count == 0:
                majority_value = num
                count +=1
            elif num == majority_value:
                count +=1
            else:
                count -=1
        
        return majority_value


        