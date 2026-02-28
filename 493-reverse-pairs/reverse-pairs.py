class Solution:
    def reversePairs(self,nums:List[int]) -> int:
        count,sorted_num = self._helper(nums)
        return count
    def _helper(self, nums: List[int]) :
        if len(nums) <=1:
            return 0,nums
        mid = len(nums) //2
        left_arr = nums[: mid]
        right_arr = nums[mid:]
        left_count , left = self._helper(left_arr)
        right_count ,right = self._helper(right_arr)
        total_count = left_count +right_count
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j+=1
            total_count +=j

        return self.merge_sort(total_count,left ,right)



    def merge_sort(self,total_count,left,right):
        result = []
        l = 0
        r = 0
        n = len(left)
        m = len(right)
        count = total_count
        
        
        while l<n and r < m:
            if left[l] < right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
            
        while l<n:
            result.append(left[l])
            l+=1
        while r<m:
            result.append(right[r])
            r+=1
        return count,result

            

