# class Solution:
#     def findDuplicate(self, nums):
#         left, right = 1, len(nums) - 1

#         while left < right:
#             mid = (left + right) // 2

#             count = 0
#             for num in nums:
#                 if num <= mid:
#                     count += 1

#             if count > mid:
#                 right = mid
#             else:
#                 left = mid + 1

#         return left


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow