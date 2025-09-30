from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dict_students = Counter(students)
        res = len(students)
        for s in sandwiches:
            if dict_students[s] > 0:
                dict_students[s] -= 1
                res -=1
            else:
                return res
        return res
        
        