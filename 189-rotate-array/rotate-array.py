class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # n=len(nums)
        # k= k%n
        # if k ==0 : return 

        # def reveal(l,r):
        #     while l<=r:
        #         nums[l] ,nums [ r] = nums[r] ,nums[l]
        #         l=l+1
        #         r=r-1
        # reveal(0,n-1)
        # reveal(0,k-1)
        # reveal(k,n-1)
        ''' for this we need to rotate the element for k step 
        BF we can do pop form right and insert on left in a list insert takes O(n) time for every element 
        so ti will take O(n*k)
        '''
        for _ in range(k):
            pop_element = nums.pop()
            nums.insert(0, pop_element)
        

