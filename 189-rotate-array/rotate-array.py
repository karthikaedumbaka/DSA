class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n  # Handle cases where k > n
        # nums[:] = nums[-k:] + nums[:-k]
        # return nums
        # # time o(n)
        #space O(1)


        n=len(nums)
        k= k%n

        def reveal(l,r):
            while l<=r:
                nums[l] ,nums [ r] = nums[r] ,nums[l]
                l=l+1
                r=r-1
        reveal(0,n-1)
        reveal(0,k-1)
        reveal(k,n-1)