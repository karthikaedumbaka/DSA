class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset_output=[]
        nums.sort() 
        def helper(nums,output):
            if len(nums)==0:
                subset_output.append(output)
                return
            op1 = output[:]
            op2 = output[:]
            op2.append(nums[0])
            helper(nums[1:],op1)
            helper(nums[1:],op2)
        helper(nums,[])
        return list(set(map(tuple, subset_output))) 

# time 2^N
# space O(n)



        