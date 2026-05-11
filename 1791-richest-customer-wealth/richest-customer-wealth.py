class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = float("-inf")
        i = len(accounts)
        j = len(accounts[0])
        for row in range(i):
            summ = 0 
            for col in range(j):
                summ += accounts[row][col]
            maxx = max(maxx,summ)
        return maxx
        # time O(n*m)
        # space O(1)
                
        