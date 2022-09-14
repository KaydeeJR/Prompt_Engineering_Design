
CREATE TABLE IF NOT EXISTS `NewsArticles` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `Domain` VARCHAR(1000) NOT NULL,
    `Title` VARCHAR(1000) NOT NULL,
    `Description` TEXT NOT NULL,
    `Body` TEXT NOT NULL,
    `Link` VARCHAR(1000) NOT NULL,
    `Timestamp` TIMESTAMP NOT NULL,
    `Analyst_Average_Score` INT DEFAULT NULL,
    `Analyst_Rank` INT DEFAULT NULL,
    `Reference_Final_Score` FLOAT DEFAULT NULL,
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;