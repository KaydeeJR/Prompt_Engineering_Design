
CREATE TABLE IF NOT EXISTS `JobsDesc` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `Document` TEXT NOT NULL,
    `Tokens` TEXT NOT NULL,
    `Relations` TEXT NOT NULL,
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;