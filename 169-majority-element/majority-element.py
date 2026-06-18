
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majortiyElement = 0 
        count = 0
        for num in nums:
            if count==0:
                majortiyElement = num
                count +=1
            elif num == majortiyElement:
                count+=1
            else:
                count -=1
        return majortiyElement
            
    # time O(n)
    # space O(1)

        