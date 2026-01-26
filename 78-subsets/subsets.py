class Solution:
    def solve(self,index:int,nums:List[int],sub_set:List[List[int]],result:List[List[int]]) -> List[List[int]]:
        # base case 
        if index >=len(nums):
            result.append(sub_set.copy())
            return
        sub_set.append(nums[index])
        self.solve(index+1,nums,sub_set,result)
        sub_set.pop()
        self.solve(index+1,nums,sub_set,result)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(0,nums,[],result)
        return result
        