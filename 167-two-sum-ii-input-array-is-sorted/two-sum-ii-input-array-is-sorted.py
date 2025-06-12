class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i < j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1] # +1 becase it is given as 1-indexed array
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1
        return [0,0]

        # time O(n)
        #space O(1)
        