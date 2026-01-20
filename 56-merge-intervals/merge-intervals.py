class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first we will sort the value , because while we are campering the starting and ending pointer of the list we need the sort value right 
        intervals.sort() # sorted the value # Time  O(NlogN)
        ans = []
        i =0
        while i < (len(intervals)):
            #s is for startng point of the interval and e is the ending pointer of interval 
            # new we are check is out curr end is  greater than the cuur_next starting pointer if yes just meage by using max for the curr ending point to curr_next ending point 
            s = intervals[i][0]
            e = intervals[i][1]
            while i < len(intervals) and intervals[i][0] <= e:
                e = max (e,intervals[i][1])
                i+=1
            # if there is no Merging point of cuur and curr_next , append the s and e pointer
            ans.append([s,e])
        return ans


        