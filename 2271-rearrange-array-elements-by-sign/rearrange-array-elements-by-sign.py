class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveIndex = 0 
        negativeIndex = 1
        output = [0]*len(nums)
        for num in nums:
            if num >= 0 :
                output[positiveIndex] = num
                positiveIndex +=2
            else:
                output[negativeIndex] = num
                negativeIndex +=2
        return output
