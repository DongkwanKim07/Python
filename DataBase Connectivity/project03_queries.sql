--  DROP SCHEMA IF EXISTS `PythonProject`;
--  CREATE SCHEMA IF NOT EXISTS `PythonProject` DEFAULT CHARACTER SET utf8mb4;
--  DROP USER IF EXISTS `Python`@`localhost`;
--  CREATE USER IF NOT EXISTS 'Python'@'localhost' IDENTIFIED BY 'Python';
--  GRANT ALL ON `PythonProject`.* TO 'Python'@'localhost';

drop table `PythonProject`.`AtlanticCod`;

USE `PythonProject`;
CREATE TABLE IF NOT EXISTS `PythonProject`.`AtlanticCod` (
  `id` INT NOT NULL auto_increment,
  `source` VARCHAR(50) NOT NULL,
  `latin_name` VARCHAR(50) NOT NULL,
  `english_name` VARCHAR(50) NOT NULL,
  `french_name` VARCHAR(50) NOT NULL,
  `year` VARCHAR(30) NOT NULL,
  `month` VARCHAR(30) NOT NULL,
  `number_otoliths` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','3','72');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','5','140');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','7','164');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','8','194');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','9','127');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','10','180');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1949','6','350');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1949','7','180');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1949','8','534');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1949','9','806');
-- INSERT INTO `pythonproject`.`atlanticcod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1949','10','60');
