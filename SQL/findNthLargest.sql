-- TO find nth largest Or 2nd maximum salary.
SELECT * FROM emp ORDER BY salary DESC OFFSET 1 LIMIT 1;