USE fkp8mn_db;

CREATE TABLE animals (
    animal_id INT PRIMARY KEY,
    name VARCHAR(50),
    species VARCHAR(50),
    age INT
);

CREATE TABLE visits (
    visit_id INT PRIMARY KEY,
    animal_id INT,
    visit_date DATETIME,
    reason TEXT,
    FOREIGN KEY (animal_id) REFERENCES animals(animal_id)
);

INSERT INTO animals VALUES (1,'Buddy','Dog',5);
INSERT INTO animals VALUES (2,'Whiskers','Cat',3);
INSERT INTO animals VALUES (3,'Charlie','Dog',7);
INSERT INTO animals VALUES (4,'Bella','Dog',2);
INSERT INTO animals VALUES (5,'Luna','Cat',4);
INSERT INTO animals VALUES (6,'Max','Dog',6);
INSERT INTO animals VALUES (7,'Oliver','Cat',1);
INSERT INTO animals VALUES (8,'Rocky','Dog',8);
INSERT INTO animals VALUES (9,'Milo','Cat',5);
INSERT INTO animals VALUES (10,'Daisy','Dog',3);

INSERT INTO visits VALUES (1,1,'2024-01-10','Vaccination');
INSERT INTO visits VALUES (2,2,'2024-01-12','Checkup');
INSERT INTO visits VALUES (3,3,'2024-01-15','Injury');
INSERT INTO visits VALUES (4,4,'2024-01-18','Vaccination');
INSERT INTO visits VALUES (5,5,'2024-01-20','Dental cleaning');
INSERT INTO visits VALUES (6,6,'2024-01-25','Checkup');
INSERT INTO visits VALUES (7,7,'2024-01-27','Vaccination');
INSERT INTO visits VALUES (8,8,'2024-02-01','Surgery follow-up');
INSERT INTO visits VALUES (9,9,'2024-02-05','Checkup');
INSERT INTO visits VALUES (10,10,'2024-02-10','Vaccination');
