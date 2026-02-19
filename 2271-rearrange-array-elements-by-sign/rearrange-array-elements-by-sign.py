class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # positive_num = []
        # negative_num = []
        # aforementioned_conditions = []
        # for num in nums:
        #     if num < 0 :
        #        negative_num.append(num)
        #     else:
        #         positive_num.append(num)
        
        # for idx in range(len(positive_num)):
        #     aforementioned_conditions.append(positive_num[idx])
        #     aforementioned_conditions.append(negative_num[idx])
        # return aforementioned_conditions
        # time O(n) * O(n) -> O(2n) -> O(n)
        # space O(n/2) +O(n/2) -> O(n)
        n = len(nums)
        ans = [0] *n
        positive_idx = 0
        negative_idx = 1
        for num in nums:
            if num < 0:
                ans[negative_idx] = num
                negative_idx +=2
            else:
                ans[positive_idx] = num
                positive_idx +=2
        return ans
                
        # time  O(n)
        # space O(1)
            




