class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # Remove out-of-window indices
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller numbers in k range as they are useless
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append current max to result (start adding from i >= k-1)
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
