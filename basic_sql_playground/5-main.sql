SELECT DISTINCT Person.last_name
FROM Person
INNER JOIN TVShow
on TVShow.name = "Game of Thrones";

SELECT COUNT (age) FROM Person 
Where age > 30;

SELECT *
INTO Person
FROM Eyescolor, TVShow, TVShowPerson; 

SELECT SUM (age) FROM Person;