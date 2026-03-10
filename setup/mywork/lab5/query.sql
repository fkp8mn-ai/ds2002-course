USE fkp8mn_db;

SELECT animals.name, animals.species, visits.visit_date, visits.reason
FROM animals
JOIN visits ON animals.animal_id = visits.animal_id
WHERE animals.species = 'Dog';
