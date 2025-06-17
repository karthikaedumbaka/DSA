starting_point_for_right=0 

def binary_sreach(nums,target, l , r, first_occ):
    l=0
    r=len(nums)-1
    ans=-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            if ans==-1:
                starting_point_for_right=m

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
        ans_lef=binary_sreach(nums,target,0,len(nums)-1,True)
        if ans_lef==-1:
            return [-1,-1]

        return [ans_lef,binary_sreach(nums,target,starting_point_for_right,len(nums)-1,False)]


# Time O(log n)
# Space O(1)
        