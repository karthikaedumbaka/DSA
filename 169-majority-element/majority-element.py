class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm  (it have half the element is same)
        result = count =0
        for num in nums:
            if count == 0 :
                result = num
            count = count + ( 1 if num == result else -1)
        return result
        # time 0(n)
        # space 0(1)

        