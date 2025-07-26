class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        attempts = 0

        while students and attempts < len(students):
            if(students[0] == sandwiches[0]):
                students.popleft()
                sandwiches.popleft()
                attempts = 0
            else:
                students.append(students.popleft())
                attempts += 1 
        
        return len(students)