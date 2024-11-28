-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: tp_lab
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno` (
  `id_alumno` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `dni` varchar(8) NOT NULL,
  `fecha_nacimiento` datetime NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `domicilio` varchar(45) NOT NULL,
  PRIMARY KEY (`id_alumno`),
  UNIQUE KEY `dni_UNIQUE` (`dni`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
INSERT INTO `alumno` VALUES (3,'Juan','Pérez','12345678','2007-11-28 00:00:00','123456789','Calle 1'),(4,'María','Gómez','23456789','2009-11-28 00:00:00','987654321','Calle 2'),(5,'Carlos','Fernández','34567890','2004-11-28 00:00:00','456789123','Calle 3'),(6,'Ana','Martínez','45678901','2007-11-28 00:00:00','789123456','Calle 4'),(7,'Lucía','López','56789012','2010-11-28 00:00:00','321654987','Calle 5'),(8,'Javier','García','67890123','2009-11-28 00:00:00','654987321','Calle 6'),(9,'Sofía','Rodríguez','78901234','2009-11-28 00:00:00','987321654','Calle 7'),(10,'Diego','Sánchez','89012345','2006-11-28 00:00:00','123789456','Calle 8'),(11,'Florencia','Torres','90123456','2009-11-28 00:00:00','456123789','Calle 9'),(12,'Miguel','Castro','01234567','2005-11-28 00:00:00','789456123','Calle 10'),(13,'Valeria','Álvarez','11223344','2012-11-28 00:00:00','147852369','Calle 11'),(14,'Fernando','Ramos','22334455','2006-11-28 00:00:00','369258147','Calle 12'),(15,'Laura','Romero','33445566','2009-11-28 00:00:00','258147369','Calle 13'),(16,'Gabriel','Vega','44556677','2007-11-28 00:00:00','369147258','Calle 14'),(17,'Camila','Silva','55667788','2011-11-28 00:00:00','147369258','Calle 15'),(18,'Ricardo','Ortiz','66778899','2004-11-28 00:00:00','258369147','Calle 16'),(19,'Elena','Moreno','77889900','2011-11-28 00:00:00','369258741','Calle 17'),(20,'Tomás','Herrera','88990011','2004-11-28 00:00:00','741258369','Calle 18'),(21,'Martina','Figueroa','99001122','2008-11-28 00:00:00','369741258','Calle 19'),(22,'Agustín','Ponce','00112233','2009-11-28 00:00:00','258741369','Calle 20'),(23,'Iñaqui','Agustin','01122445','2004-06-10 00:00:00','123435232','Calle 21'),(24,'Martin','Iñaqui','44444456','2005-10-06 00:00:00','1231234567','Calle 29');
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursadas`
--

DROP TABLE IF EXISTS `cursadas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursadas` (
  `id_cursada` int NOT NULL AUTO_INCREMENT,
  `curso` varchar(45) NOT NULL,
  PRIMARY KEY (`id_cursada`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursadas`
--

LOCK TABLES `cursadas` WRITE;
/*!40000 ALTER TABLE `cursadas` DISABLE KEYS */;
INSERT INTO `cursadas` VALUES (1,'Matemáticas'),(2,'Lengua'),(3,'Historia'),(4,'Física'),(5,'Química');
/*!40000 ALTER TABLE `cursadas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inscripciones`
--

DROP TABLE IF EXISTS `inscripciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inscripciones` (
  `id_inscripciones` int NOT NULL AUTO_INCREMENT,
  `id_alumno` int DEFAULT NULL,
  `id_cursada` int DEFAULT NULL,
  `fecha_inscripcion` date DEFAULT NULL,
  PRIMARY KEY (`id_inscripciones`),
  KEY `id_alumno` (`id_alumno`),
  KEY `id_cursada` (`id_cursada`),
  CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`id_alumno`),
  CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`id_cursada`) REFERENCES `cursadas` (`id_cursada`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscripciones`
--

LOCK TABLES `inscripciones` WRITE;
/*!40000 ALTER TABLE `inscripciones` DISABLE KEYS */;
INSERT INTO `inscripciones` VALUES (1,3,1,'2024-01-01'),(2,3,2,'2024-01-01'),(3,4,1,'2024-01-02'),(4,4,3,'2024-01-02'),(5,5,4,'2024-01-03'),(6,6,5,'2024-01-04'),(7,7,2,'2024-01-05'),(8,8,3,'2024-01-06'),(9,9,4,'2024-01-07'),(10,10,5,'2024-01-08'),(11,11,1,'2024-01-09'),(12,12,2,'2024-01-10'),(13,13,3,'2024-01-11'),(14,14,4,'2024-01-12'),(15,15,5,'2024-01-13'),(16,16,1,'2024-01-14'),(17,17,2,'2024-01-15'),(18,18,3,'2024-01-16'),(19,19,4,'2024-01-17'),(20,20,5,'2024-01-18'),(22,22,5,'2024-11-26');
/*!40000 ALTER TABLE `inscripciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-28 13:32:29
