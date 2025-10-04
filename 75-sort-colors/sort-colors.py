class Solution:
    # def sort_arr(self, left, right):
    #     result = []
    #     i, j = 0, 0
    #     n, m = len(left), len(right)

    #     while i < n and j < m:
    #         if left[i] <= right[j]:
    #             result.append(left[i])
    #             i += 1
    #         else:
    #             result.append(right[j])
    #             j += 1

    #     while i < n:
    #         result.append(left[i])
    #         i += 1
    #     while j < m:
    #         result.append(right[j])
    #         j += 1

    #     return result

    # def merge_sort(self, nums):
    #     if len(nums) <= 1:
    #         return nums

    #     mid = len(nums) // 2
    #     left = self.merge_sort(nums[:mid])
    #     right = self.merge_sort(nums[mid:])
    #     return self.sort_arr(left, right)

    # def sortColors(self, nums: List[int]) -> None:
    #     sorted_nums = self.merge_sort(nums)
    #     # Modify in-place
    #     for i in range(len(nums)):
    #         nums[i] = sorted_nums[i]
    #     # time n(longn)
    #     # space o(1)
    def sortColors(self, nums: List[int]) -> None:
        l,i,r=0,0,len(nums)-1
        while i<=r:
            if nums[i] == 0 :
                nums[l] , nums[i] = nums[i] ,nums[l]
                l+=1
            elif nums[i] ==2:
                nums[r] , nums[i] = nums[i] ,nums[r]
                r-=1
                i-=1
            i+=1
        return nums


    