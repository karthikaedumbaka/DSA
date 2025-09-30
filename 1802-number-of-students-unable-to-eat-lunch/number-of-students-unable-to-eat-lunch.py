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
        # time O(n)
        # space O(1)
'''Problem Statement (simplified)

You have students in a queue, each with a preferred sandwich type (0 or 1).

You have a stack of sandwiches, each also 0 or 1.

Students try to take the sandwich on top of the stack:

If the sandwich matches their preference, they take it and leave the queue.

If not, the student moves to the end of the queue.

The process stops when none of the students in the queue want the top sandwich.

Goal: return the number of students unable to eat.'''