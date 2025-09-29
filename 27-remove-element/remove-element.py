class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[k]= nums[i]
                k+=1
        return k

'''
val = 3
k=0 , i =0 , num[i] != val -> 3 != 3 (False) => [3,2,2,3]
k=0 , i = 1 ,num[i] != val -> 2 != 3 (True)  ==> [2,2,2,3] ......k=1
k=1 ,i=2 ,num[i] != val -> 2 != 3 (True)  ==> [2,2,2,3] ......k=2
k=1 ,i=3 ,num[i] != val -> 3 != 3 (False)  ==> [2,2,2,3] ......k=2


'''
        