class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.helper(nums, 0, n - 1)
        self.helper(nums, 0, k - 1)
        self.helper(nums, k, n - 1)

    def helper(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1