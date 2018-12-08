/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 10.1.35-MariaDB : Database - db_simak
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_simak` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_simak`;

/*Table structure for table `dim_fakultas` */

DROP TABLE IF EXISTS `dim_fakultas`;

CREATE TABLE `dim_fakultas` (
  `id_fakultas` int(11) NOT NULL AUTO_INCREMENT,
  `nm_fakultas` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_fakultas`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `dim_fakultas` */

insert  into `dim_fakultas`(`id_fakultas`,`nm_fakultas`) values (1,'teknik'),(2,'kedokteran'),(3,'ekonomi dan bisnis'),(4,'peternakan'),(5,'kedokteran hewan'),(6,'teknologi pertanian'),(7,'test'),(8,'tost'),(9,'tist'),(10,'tuk');

/*Table structure for table `dim_kabupaten` */

DROP TABLE IF EXISTS `dim_kabupaten`;

CREATE TABLE `dim_kabupaten` (
  `id_kabupaten` int(11) NOT NULL AUTO_INCREMENT,
  `nm_kabupaten` varchar(50) DEFAULT NULL,
  `id_provinsi` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_kabupaten`),
  KEY `id_provinsi` (`id_provinsi`),
  CONSTRAINT `dim_kabupaten_ibfk_1` FOREIGN KEY (`id_provinsi`) REFERENCES `dim_provinsi` (`id_provinsi`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `dim_kabupaten` */

insert  into `dim_kabupaten`(`id_kabupaten`,`nm_kabupaten`,`id_provinsi`) values (1,'denpasar',1),(2,'bangli',1),(3,'tabanan',1),(4,'karangasem',1),(5,'jembrana',1),(6,'singaraja',1),(7,'gianyar',1),(8,'klungkung',1),(9,'badung',1),(10,'sempidi',1),(11,'test',2),(12,'tost',2),(13,'hai',2);

/*Table structure for table `dim_mahasiswa` */

DROP TABLE IF EXISTS `dim_mahasiswa`;

CREATE TABLE `dim_mahasiswa` (
  `id_mhs` int(11) NOT NULL AUTO_INCREMENT,
  `NIM` varchar(11) DEFAULT NULL,
  `nama_mhs` varchar(50) DEFAULT NULL,
  `alamat` varchar(50) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `tempat_lahir` varchar(50) DEFAULT NULL,
  `no_telp` char(13) DEFAULT NULL,
  `agama` varchar(30) DEFAULT NULL,
  `jenis_kelamin` varchar(20) DEFAULT NULL,
  `status_bekerja` enum('sudah_bekerja','belum_bekerja') DEFAULT NULL,
  `status_perkawinan` enum('belum_kawin','sudah_kawin') DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `id_kabupaten` int(11) DEFAULT NULL,
  `id_pa` int(11) DEFAULT NULL,
  `id_prodi` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_mhs`),
  KEY `id_prodi` (`id_prodi`),
  KEY `id_pa` (`id_pa`),
  KEY `id_kabupaten` (`id_kabupaten`),
  CONSTRAINT `dim_mahasiswa_ibfk_2` FOREIGN KEY (`id_prodi`) REFERENCES `dim_prodi` (`id_prodi`),
  CONSTRAINT `dim_mahasiswa_ibfk_3` FOREIGN KEY (`id_pa`) REFERENCES `dim_pa` (`id_PA`),
  CONSTRAINT `dim_mahasiswa_ibfk_5` FOREIGN KEY (`id_kabupaten`) REFERENCES `dim_kabupaten` (`id_kabupaten`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `dim_mahasiswa` */

insert  into `dim_mahasiswa`(`id_mhs`,`NIM`,`nama_mhs`,`alamat`,`tgl_lahir`,`tempat_lahir`,`no_telp`,`agama`,`jenis_kelamin`,`status_bekerja`,`status_perkawinan`,`email`,`id_kabupaten`,`id_pa`,`id_prodi`) values (1,'1605551068','Ni Putu Ayu Widiari','denpasar','2018-11-14','denpasar','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','widiariayyu@gmail.com',1,1,1),(2,'1605551062','Laurensius Adi Kurniawan','denpasar','1997-10-25','melbourne','081237723316','katolik','laki-laki','belum_bekerja','belum_kawin','adikur62@gmail.com',5,2,2),(3,'1605551058','Praba Hridayami','denpasar','1997-12-10','mengwi','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','praba@gmail.com',2,1,4),(4,'1605551055','Ria Mandasari','mengwi','1998-07-15','badung','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','gek.ria@gmail.com',9,1,1),(5,'1605551068','Agastya Harta','jakarta','1998-08-10','tabanan','081237723316','hindu','laki-laki','belum_bekerja','belum_kawin','agash@gmail.com',3,1,1),(6,'1605551012','Yonatan ZT','badung','1998-05-23','denpasar','081237723316','kristen','laki-laki','belum_bekerja','belum_kawin','natanzt@gmail.com',4,1,5),(7,'1605551045','Savita','tabanan','1998-06-20','klungkung','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','savita.ajach@gmail.com',8,1,1),(8,'1605551070','Veggy','amerika','1998-04-12','gianyar','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','veggy.h@gmail.com',7,1,1),(9,'1605551043','Trio Putra','london','1998-06-12','denpasar','081237723316','hindu','laki-laki','belum_bekerja','belum_kawin','trio@gmail.com',6,3,3),(10,'1605551082','Krisna Arynasta','denpasar','1998-06-13','denpasar','089765432111','hindu','laki-laki','belum_bekerja','belum_kawin','krisna@gmail.com',3,2,1),(11,'1605551078','tokek','deps','2018-12-08','denpasar','089777635267','hindu','laki-laki','belum_bekerja','belum_kawin','tick@gmail.com',3,4,1),(12,'1605551068','Ni Putu Ayu Widiari','denpasar','2018-11-14','denpasar','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','widiariayyu@gmail.com',1,1,1),(13,'1605551062','Laurensius Adi Kurniawan','denpasar','1997-10-25','melbourne','081237723316','katolik','laki-laki','belum_bekerja','belum_kawin','adikur62@gmail.com',5,2,2),(14,'1605551058','Praba Hridayami','denpasar','1997-12-10','mengwi','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','praba@gmail.com',2,1,4),(15,'1605551055','Ria Mandasari','mengwi','1998-07-15','badung','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','gek.ria@gmail.com',9,1,1),(16,'1605551068','Agastya Harta','jakarta','1998-08-10','tabanan','081237723316','hindu','laki-laki','belum_bekerja','belum_kawin','agash@gmail.com',3,1,1),(17,'1605551012','Yonatan ZT','badung','1998-05-23','denpasar','081237723316','kristen','laki-laki','belum_bekerja','belum_kawin','natanzt@gmail.com',4,1,5),(18,'1605551045','Savita','tabanan','1998-06-20','klungkung','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','savita.ajach@gmail.com',8,1,1),(19,'1605551070','Veggy','amerika','1998-04-12','gianyar','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','veggy.h@gmail.com',7,1,1),(20,'1605551043','Trio Putra','london','1998-06-12','denpasar','081237723316','hindu','laki-laki','belum_bekerja','belum_kawin','trio@gmail.com',6,3,3),(21,'1605551082','Krisna Arynasta','denpasar','1998-06-13','denpasar','089765432111','hindu','laki-laki','belum_bekerja','belum_kawin','krisna@gmail.com',3,2,1),(22,'1605551078','tokek','deps','2018-12-08','denpasar','089777635267','hindu','laki-laki','belum_bekerja','belum_kawin','tick@gmail.com',3,4,1),(23,'1605551061','reyhan','deps','2018-12-08','denpasar','089765425268','hindu','laki-laki','belum_bekerja','belum_kawin','reyrey@gmail.com',2,4,1);

/*Table structure for table `dim_matkul` */

DROP TABLE IF EXISTS `dim_matkul`;

CREATE TABLE `dim_matkul` (
  `id_matkul` int(11) NOT NULL AUTO_INCREMENT,
  `kode_matkul` varchar(20) DEFAULT NULL,
  `nama_matkul` varchar(30) DEFAULT NULL,
  `sks` float DEFAULT NULL,
  PRIMARY KEY (`id_matkul`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `dim_matkul` */

insert  into `dim_matkul`(`id_matkul`,`kode_matkul`,`nama_matkul`,`sks`) values (1,'C01','Computer Vision',3),(2,'D01','Datawarehouse',3),(3,'D02','Data Mining',3),(4,'I01','IOT',3),(5,'S01','STKI',3),(6,'T01','Teknologi Sensor Divais',3),(7,'E01','Etika Profesi dan Korupsi',3),(8,'R01','Rekayasa Perangkat Lunak',3),(9,'N01','Natural Language Processing',3),(10,'M01','Machine Learning',3),(11,'k01','test',2),(12,'k02','tost',3),(13,'k03','ticikk',3),(14,'k04','tokek',3),(15,'k05','puki',3),(16,'k06','colok',3),(17,'k07','puki',3),(18,'k08','plis',3),(19,'k09','maulah',3),(20,'k10','yoloh',3),(21,'k11','topai',2),(22,'k12','mau yaoloo',2);

/*Table structure for table `dim_pa` */

DROP TABLE IF EXISTS `dim_pa`;

CREATE TABLE `dim_pa` (
  `id_PA` int(11) NOT NULL AUTO_INCREMENT,
  `nama_PA` varchar(50) DEFAULT NULL,
  `alamat` varchar(50) DEFAULT NULL,
  `no_telp` char(13) DEFAULT NULL,
  PRIMARY KEY (`id_PA`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `dim_pa` */

insert  into `dim_pa`(`id_PA`,`nama_PA`,`alamat`,`no_telp`) values (1,'Agung Oka','denpasar','0897765478'),(2,'Agung Cahyawan','badung','0897665432'),(3,'Bayupati','denpasar','0832938282'),(4,'Suwija Putra','denpasar','0812938293'),(5,'Ayu Wirdiani','denpasar','0897654231'),(6,'I Kadek Gunawan','denpasar','0897654312'),(7,'praba hridayamin','denpasar','0897654352'),(8,'test','dps','0897654321'),(9,'coba','deps','0987653426'),(10,'tokek','deps','0897653425'),(11,'hai','tolol','08973892392'),(12,'tost','tolollll','08976368939'),(13,'tololl','hai','08543758904');

/*Table structure for table `dim_prodi` */

DROP TABLE IF EXISTS `dim_prodi`;

CREATE TABLE `dim_prodi` (
  `id_prodi` int(11) NOT NULL AUTO_INCREMENT,
  `nm_prodi` varchar(50) DEFAULT NULL,
  `id_fakultas` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_prodi`),
  KEY `id_fakultas` (`id_fakultas`),
  CONSTRAINT `dim_prodi_ibfk_1` FOREIGN KEY (`id_fakultas`) REFERENCES `dim_fakultas` (`id_fakultas`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `dim_prodi` */

insert  into `dim_prodi`(`id_prodi`,`nm_prodi`,`id_fakultas`) values (1,'teknologi informasi',1),(2,'teknik arsitektur',1),(3,'teknik sipil',1),(4,'teknik mesin',1),(5,'teknik elektro',2),(6,'kedokteran umum',2),(7,'kedokteran hewan',2),(8,'peternakan',1),(9,'tost',3),(10,'tisi',3),(11,'tiktok',2);

/*Table structure for table `dim_provinsi` */

DROP TABLE IF EXISTS `dim_provinsi`;

CREATE TABLE `dim_provinsi` (
  `id_provinsi` int(11) NOT NULL AUTO_INCREMENT,
  `nm_provinsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_provinsi`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `dim_provinsi` */

insert  into `dim_provinsi`(`id_provinsi`,`nm_provinsi`) values (1,'bali'),(2,'kalimantan utara'),(3,'kalimantan selatan'),(4,'tost'),(5,'tick'),(6,'prok');

/*Table structure for table `dim_semester` */

DROP TABLE IF EXISTS `dim_semester`;

CREATE TABLE `dim_semester` (
  `id_semester` int(11) NOT NULL AUTO_INCREMENT,
  `nm_semester` varchar(20) DEFAULT NULL,
  `tahun_ajaran` year(4) DEFAULT NULL,
  PRIMARY KEY (`id_semester`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `dim_semester` */

insert  into `dim_semester`(`id_semester`,`nm_semester`,`tahun_ajaran`) values (1,'Ganjil',2018),(2,'Genap',2018),(3,'Pendek',2018),(4,'Remidi',2018),(5,'test',2019),(6,'tost',2018);

/*Table structure for table `fact_khs` */

DROP TABLE IF EXISTS `fact_khs`;

CREATE TABLE `fact_khs` (
  `id_fact_khs` int(11) NOT NULL AUTO_INCREMENT,
  `id_semester` int(11) DEFAULT NULL,
  `id_mhs` int(11) DEFAULT NULL,
  `id_matkul` int(11) DEFAULT NULL,
  `nilai` float DEFAULT NULL,
  `indeks` varchar(11) DEFAULT NULL,
  `IPS` float DEFAULT NULL,
  `IPK` float DEFAULT NULL,
  PRIMARY KEY (`id_fact_khs`),
  KEY `id_semester` (`id_semester`),
  KEY `id_mhs` (`id_mhs`),
  KEY `id_matkul` (`id_matkul`),
  CONSTRAINT `fact_khs_ibfk_2` FOREIGN KEY (`id_mhs`) REFERENCES `dim_mahasiswa` (`id_mhs`),
  CONSTRAINT `fact_khs_ibfk_4` FOREIGN KEY (`id_semester`) REFERENCES `dim_semester` (`id_semester`),
  CONSTRAINT `fact_khs_ibfk_5` FOREIGN KEY (`id_matkul`) REFERENCES `dim_matkul` (`id_matkul`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `fact_khs` */

insert  into `fact_khs`(`id_fact_khs`,`id_semester`,`id_mhs`,`id_matkul`,`nilai`,`indeks`,`IPS`,`IPK`) values (1,1,1,1,10.5,'B+',3.625,3.625),(2,1,1,2,12,'A',3.625,3.625),(3,1,1,3,10.5,'B+',3.625,3.625),(4,1,1,2,10.5,'B+',3.625,3.625),(5,2,1,4,12,'A',3.5,3.5625),(6,2,1,5,9,'B',3.5,3.5625),(7,1,2,1,12,'A',3.83333,3.83333),(8,1,2,2,12,'A',3.83333,3.83333),(9,1,2,3,10.5,'B+',3.83333,3.83333),(10,2,2,1,10.5,'B',3,3.41667),(11,2,2,2,9,'B',3,3.41667),(12,2,2,3,7.5,'C+',3,3.41667),(13,1,3,1,10.5,'B+',3.5,3.5),(14,1,3,2,9,'B',3.5,3.5),(15,1,3,3,12,'A',3.5,3.5),(16,2,3,1,9,'B',2.75,3.125),(17,2,3,2,7.5,'C+',2.75,3.125),(18,1,1,2,10.5,'B+',3.625,3.625),(19,2,3,1,9,'B',2.75,2.75),(20,2,3,2,7.5,'C+',2.75,2.75);

/*Table structure for table `fact_krs` */

DROP TABLE IF EXISTS `fact_krs`;

CREATE TABLE `fact_krs` (
  `id_fact_krs` int(11) NOT NULL AUTO_INCREMENT,
  `id_matkul` int(11) DEFAULT NULL,
  `id_mhs` int(11) DEFAULT NULL,
  `id_semester` int(11) DEFAULT NULL,
  `total_sks` float DEFAULT NULL,
  PRIMARY KEY (`id_fact_krs`),
  KEY `id_semester` (`id_semester`),
  KEY `id_mhs` (`id_mhs`),
  KEY `id_matkul` (`id_matkul`),
  CONSTRAINT `fact_krs_ibfk_10` FOREIGN KEY (`id_matkul`) REFERENCES `dim_matkul` (`id_matkul`),
  CONSTRAINT `fact_krs_ibfk_7` FOREIGN KEY (`id_mhs`) REFERENCES `dim_mahasiswa` (`id_mhs`),
  CONSTRAINT `fact_krs_ibfk_9` FOREIGN KEY (`id_semester`) REFERENCES `dim_semester` (`id_semester`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;

/*Data for the table `fact_krs` */

insert  into `fact_krs`(`id_fact_krs`,`id_matkul`,`id_mhs`,`id_semester`,`total_sks`) values (2,1,1,1,3),(3,1,1,1,3),(4,2,1,1,3),(5,3,2,1,3),(6,4,2,1,3),(7,1,1,1,10.5),(8,1,1,2,12),(9,1,1,3,10.5),(10,1,1,2,10.5),(11,2,1,4,12),(12,2,1,5,9),(13,1,2,1,12),(14,1,2,2,12),(15,1,2,3,10.5),(16,2,2,1,10.5),(17,2,2,2,9),(18,2,2,3,7.5),(19,1,3,1,10.5),(20,1,3,2,9),(21,1,3,3,12),(22,2,3,1,9),(23,2,3,2,7.5),(24,1,1,1,10.5),(25,1,1,2,12),(26,1,1,3,10.5),(27,1,1,2,10.5),(28,2,1,4,12),(29,2,1,5,9),(30,1,2,1,12),(31,1,2,2,12),(32,1,2,3,10.5),(33,2,2,1,10.5),(34,2,2,2,9),(35,2,2,3,7.5),(36,1,3,1,10.5),(37,1,3,2,9),(38,1,3,3,12),(39,2,3,1,9),(40,2,3,2,7.5),(41,1,1,1,10.5),(42,1,1,2,12),(43,1,1,3,10.5),(44,1,1,2,10.5),(45,2,1,4,12),(46,2,1,5,9),(47,1,2,1,12),(48,1,2,2,12),(49,1,2,3,10.5),(50,2,2,1,10.5),(51,2,2,2,9),(52,2,2,3,7.5),(53,1,3,1,10.5),(54,1,3,2,9),(55,1,3,3,12),(56,2,3,1,9),(57,2,3,2,7.5);

/*Table structure for table `update_log` */

DROP TABLE IF EXISTS `update_log`;

CREATE TABLE `update_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `master_id` int(11) DEFAULT NULL,
  `master_name` varchar(20) DEFAULT NULL,
  `start_row` int(11) DEFAULT NULL,
  `end_row` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `update_log` */

insert  into `update_log`(`id`,`date`,`master_id`,`master_name`,`start_row`,`end_row`) values (1,'2018-12-08 13:10:06',1,'dim_fakultas',1,9),(2,'2018-12-08 13:10:06',2,'dim_provinsi',1,5),(3,'2018-12-08 13:10:06',3,'dim_kabupaten',1,12),(4,'2018-12-08 13:10:06',4,'dim_pa',1,10),(5,'2018-12-08 13:10:06',5,'dim_semester',1,5),(6,'2018-12-08 13:10:06',7,'dim_prodi',1,10),(7,'2018-12-08 13:10:06',8,'dim_mahasiswa',1,11),(8,'2018-12-08 13:11:40',6,'dim_matkul',1,21),(9,'2018-12-08 13:11:40',9,'fact_krs',1,4),(10,'2018-12-08 13:11:40',10,'fact_khs',1,2),(11,'2018-12-08 13:12:13',9,'fact_krs',8,51),(12,'2018-12-08 13:12:13',10,'fact_khs',18,20),(13,'2018-12-08 13:12:42',6,'dim_matkul',22,22),(14,'2018-12-08 13:12:42',9,'fact_krs',24,51),(15,'2018-12-08 14:01:21',5,'dim_semester',6,6),(16,'2018-12-08 14:01:21',9,'fact_krs',41,51),(17,'2018-12-08 14:08:49',4,'dim_pa',11,0),(18,'2018-12-08 14:26:27',1,'dim_fakultas',10,10),(19,'2018-12-08 14:26:27',2,'dim_provinsi',6,6),(20,'2018-12-08 14:26:27',3,'dim_kabupaten',13,13),(21,'2018-12-08 14:26:59',7,'dim_prodi',11,11),(22,'2018-12-08 14:26:59',8,'dim_mahasiswa',12,12),(23,'2018-12-08 14:28:05',4,'dim_pa',1,12),(24,'2018-12-08 14:53:54',4,'dim_pa',13,13);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
