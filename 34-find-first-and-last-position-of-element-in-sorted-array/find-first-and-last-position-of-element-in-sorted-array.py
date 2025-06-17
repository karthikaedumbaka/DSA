def binary_sreach(nums,target, l , r, first_occ):
    l=0
    r=len(nums)-1
    ans=-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            ans = m
            if first_occ:
                r=m-1
            else:
                l=m+1
        elif nums[m] < target:
            l=m+1
        else:
            r=m-1
    return ans


class Solution(object):
    def searchRange(self, nums, target):
        return [binary_sreach(nums,target,0,len(nums)-1,True),binary_sreach(nums,target,0,len(nums)-1,False)]
        