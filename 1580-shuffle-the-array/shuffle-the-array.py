class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=1*n
        result_arr = []
        for i in range(len(nums)//2):
            result_arr.append(nums[i])
            result_arr.append(nums[j])
            i+=1
            j+=1
        return result_arr