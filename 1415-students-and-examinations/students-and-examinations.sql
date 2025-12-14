# Write your MySQL query statement below
select s.student_id, s.student_name, sub.subject_name, COUNT(e.subject_name) as attended_exams 
FROM students s 
cross join subjects sub
left join examinations e 
on s.student_id = e.student_id
and sub.subject_name = e.subject_name
group by s.student_id, s.student_name, sub.subject_name
order by s.student_id, sub.subject_name;