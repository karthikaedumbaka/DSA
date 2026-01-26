class Solution:
    def solve(self,index:int,nums:List[int],sub_set:List[List[int]],result:List[List[int]]) -> List[List[int]]:
        # base case 
        if index >=len(nums):
            #if the index is greater than or equal to length copy the subset
            result.append(sub_set.copy())
            return
        # if not append the value to sub_sub using the index
        sub_set.append(nums[index])
        # update the index +1 
        self.solve(index+1,nums,sub_set,result)
        #after backtrack pop the latest value
        sub_set.pop()
        
        self.solve(index+1,nums,sub_set,result)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(0,nums,[],result)
        return result
        