CREATE SCHEMA `crud` ;

CREATE TABLE `crud`.`students` ( 
  `Id_num` VARCHAR(9) NOT NULL PRIMARY KEY,
  `Firstname` VARCHAR(45) NULL,
  `Lastname` VARCHAR(45) NULL,
  `Course` VARCHAR(45) NULL,
  `Year` VARCHAR(45) NULL, 
  `Gender` VARCHAR(45) NULL)

INSERT INTO `crud`.`students`
(`ID`,
`Firstname`,
`Lastname`, 
`Course`,
`Year`,
`Gender`
) VALUES (1, 'Angelique', 'Canete', 'BSCS', '3rd yr', 'F');

SELECT Course
FROM Course

CREATE TABLE `crud`.`college` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NULL,
  `name` VARCHAR(255) NULL,
  PRIMARY KEY (`id`));
  
  INSERT INTO `crud`.`college`
(`id`,
`code`,
`name`
) VALUES (1, 'CCS', 'College of Computer Studies'), 
(2, 'COET', 'College of Engineering and Technology'),
 (3, 'CASS', 'College of Social Sciences'),
 (4, 'CON', 'College of Nursing'),
 (5, 'CBAA', 'College of Business Administration and Accountancy'),
 (6, 'CSM', 'College of Science and Mathematics');
 


  
  CREATE TABLE `crud`.`course` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(255) NULL,
  `name` VARCHAR(255) NULL,
  `college` VARCHAR (255) NULL,
  PRIMARY KEY (`id`));
  
	INSERT INTO `crud`.`course` ( 
    `id`,
    `code`,
    `name`,
    `college`
    ) VALUES ( '1', 'BSCS', 'Bachelor of Science in Computer Studies','College of Computer Studies'),
    (2,'BSA','Bachelor of Sceince in Accountancy', 'College of Business Administration and Accountancy'),
    (3,'BSCOMENG', 'Bachelor of Science in Computer Engineering', 'College of Engineering and Technology'),
    (4,'BASOCIO', 'Bachelor of Arts in Sociology','College of Social Sciences'),
    (5,'BSN','Bachelor of Science in Nursing', 'College of Nursing'),
    (6,'BSSTAT','Bachelor of Science in Statistics','College of Science and Mathematics');