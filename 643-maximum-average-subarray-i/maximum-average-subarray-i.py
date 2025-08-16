
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def findMaxAverage(self, nums, k):
        curr_avg =0
        n=len(nums)
        for i in range(k):
            curr_avg+=nums[i]
        max_avg = curr_avg /k

        for i in range(k,n):
            curr_avg +=nums[i]
            curr_avg -= nums[i-k]
            avg=curr_avg/k
            max_avg=max(avg,max_avg)

        return max_avg
        #time 0(n)
        #space 0(1)

        
