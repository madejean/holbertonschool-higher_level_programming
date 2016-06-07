SELECT DISTINCT last_name
FROM Person
INNER JOIN TVShowPerson on Person.id = TVShowPerson.person_id
INNER JOIN TVshow on TVShowPerson.tvshow_id = TVshow.id
WHERE TVshow.name = 'Game of Thrones' 
ORDER BY Person.last_name;

SELECT COUNT (age) FROM Person 
Where age > 30;

SELECT Person.id, first_name, last_name, age, color, name
FROM Person
INNER JOIN EyesColor on Person.id = EyesColor.person_id
INNER JOIN TVShowPerson on Person.id = TVShowPerson.person_id
INNER JOIN TVShow on TVShowPerson.tvshow_id = TVShow.id;

SELECT SUM (age) FROM Person;
