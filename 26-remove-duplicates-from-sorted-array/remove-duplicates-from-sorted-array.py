class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # BF 
        '''
        use unique and update the same variable
        '''
        # new_nums = list(set(nums))
        # nums[:len(new_nums)] =  new_nums
        # return  len(new_nums)
        # time O(1)
        # space O(n)
        i=1 # check for length of unique number lenght
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:   # checking for defense
                nums[i] = nums[j]
                i+=1
        return i 