class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_num = []
        negative_num = []
        aforementioned_conditions = []
        for num in nums:
            if num < 0 :
               negative_num.append(num)
            else:
                positive_num.append(num)
        
        for idx in range(len(positive_num)):
            aforementioned_conditions.append(positive_num[idx])
            aforementioned_conditions.append(negative_num[idx])
        return aforementioned_conditions
