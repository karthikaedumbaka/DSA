class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # 1) Reverse entire array
        rev(0, n - 1)
        # 2) Reverse first k elements
        rev(0, k - 1)
        # 3) Reverse remaining n - k elements
        rev(k, n - 1)
