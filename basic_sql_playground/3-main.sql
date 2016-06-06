UPDATE Person
SET age = '27'
WHERE first_name = 'Jon';

UPDATE Person
SET age = '18'
WHERE first_name = 'Walter Junior';

DELETE FROM Person
WHERE first_name = 'Walter';

DELETE FROM EyesColor
WHERE person_id = 'Walter';

SELECT * FROM Person
ORDER BY first_name;