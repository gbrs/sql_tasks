

-- Можно ли использовать новосозданное поле в оконке?
SELECT
    courier_id + order_id as sm,
    SUM(sm) OVER (partition by time::DATE)
FROM
    courier_actions
-- PostgreSQL: column "sm" does not exist LINE 3
SELECT
    student_id + subject_id as sm,
    SUM(sm) OVER (partition by date_attempt)
FROM
    attempt
-- MySQL: Unknown column 'sm' in 'field list'