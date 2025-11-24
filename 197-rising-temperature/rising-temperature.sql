# Write your MySQL query statement below
select w1.id from weather w1
join weather w2
on DATE_SUB(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
WHERE w1.temperature > w2.temperature