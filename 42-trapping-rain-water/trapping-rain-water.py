class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_wall ,right_wall =0 , 0
        left_trap =[0]*n
        right_trap = [0]*n
        for i in range(n):
            j=-i-1
            left_trap[i] = left_wall
            right_trap[j] = right_wall
            left_wall = max(left_wall,height[i])
            right_wall = max(right_wall,height[j])
        summ=0
        for i in range(n):
            pot = min(left_trap[i], right_trap[i])
            summ+= max(0,pot-height[i])
        return summ

    # time O(n)
    # space O(n)
        