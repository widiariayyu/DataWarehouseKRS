/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 10.1.35-MariaDB : Database - db_akademik
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_akademik` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_akademik`;

/*Table structure for table `tb_detailkhs` */

DROP TABLE IF EXISTS `tb_detailkhs`;

CREATE TABLE `tb_detailkhs` (
  `id_detail_khs` int(11) NOT NULL AUTO_INCREMENT,
  `id_khs` int(11) DEFAULT NULL,
  `id_matkul` int(11) DEFAULT NULL,
  `nilai` float DEFAULT NULL,
  `indeks` enum('A','B+','B','C+','C','D+','D','E') DEFAULT NULL,
  PRIMARY KEY (`id_detail_khs`),
  KEY `id_khs` (`id_khs`),
  KEY `id_matkul` (`id_matkul`),
  CONSTRAINT `tb_detailkhs_ibfk_2` FOREIGN KEY (`id_khs`) REFERENCES `tb_khs` (`id_khs`),
  CONSTRAINT `tb_detailkhs_ibfk_3` FOREIGN KEY (`id_matkul`) REFERENCES `tb_matkul` (`id_matkul`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `tb_detailkhs` */

insert  into `tb_detailkhs`(`id_detail_khs`,`id_khs`,`id_matkul`,`nilai`,`indeks`) values (2,1,1,10.5,'B+'),(5,1,2,12,'A'),(6,1,3,10.5,'B+'),(7,2,4,12,'A'),(8,2,5,9,'B'),(9,3,1,10.5,'B+'),(10,3,2,9,'B'),(11,3,3,12,'A'),(12,4,1,12,'A'),(13,4,2,12,'A'),(14,4,3,10.5,'B+'),(15,5,1,10.5,'B'),(16,5,2,9,'B'),(17,5,3,7.5,'C+'),(18,6,1,9,'B'),(19,6,2,7.5,'C+'),(20,1,2,10.5,'B+');

/*Table structure for table `tb_detailkrs` */

DROP TABLE IF EXISTS `tb_detailkrs`;

CREATE TABLE `tb_detailkrs` (
  `id_detail` int(11) NOT NULL AUTO_INCREMENT,
  `id_krs` int(11) DEFAULT NULL,
  `id_matkul` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_detail`),
  KEY `id_krs` (`id_krs`),
  KEY `id_matkul` (`id_matkul`),
  CONSTRAINT `tb_detailkrs_ibfk_6` FOREIGN KEY (`id_krs`) REFERENCES `tb_krs` (`id_krs`),
  CONSTRAINT `tb_detailkrs_ibfk_7` FOREIGN KEY (`id_matkul`) REFERENCES `tb_matkul` (`id_matkul`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

/*Data for the table `tb_detailkrs` */

insert  into `tb_detailkrs`(`id_detail`,`id_krs`,`id_matkul`) values (2,1,1),(3,1,1),(4,1,2),(5,2,3),(6,2,4),(8,2,NULL),(9,3,NULL),(10,3,NULL),(11,3,NULL),(12,4,NULL),(13,4,NULL),(14,4,NULL),(15,9,NULL),(16,9,NULL),(17,10,NULL),(18,10,NULL),(19,12,NULL),(20,12,NULL),(21,5,NULL),(22,5,NULL),(23,5,NULL),(24,13,NULL),(25,13,NULL),(26,6,NULL),(27,6,NULL),(28,6,NULL),(29,14,NULL),(30,14,NULL),(31,14,NULL),(32,7,NULL),(33,7,NULL),(34,7,NULL),(35,15,NULL),(36,15,NULL),(37,15,NULL),(38,15,NULL),(39,8,NULL),(40,8,NULL),(41,8,NULL),(42,8,NULL),(43,16,NULL),(44,16,NULL),(45,16,NULL),(46,1,NULL),(47,1,NULL),(48,2,NULL),(49,2,NULL),(50,3,NULL),(51,3,NULL);

/*Table structure for table `tb_fakultas` */

DROP TABLE IF EXISTS `tb_fakultas`;

CREATE TABLE `tb_fakultas` (
  `id_fakultas` int(11) NOT NULL AUTO_INCREMENT,
  `nm_fakultas` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_fakultas`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `tb_fakultas` */

insert  into `tb_fakultas`(`id_fakultas`,`nm_fakultas`) values (1,'teknik'),(2,'kedokteran'),(3,'ekonomi dan bisnis'),(4,'peternakan'),(5,'kedokteran hewan'),(6,'teknologi pertanian'),(7,'test'),(8,'tost'),(9,'tist'),(10,'tuk');

/*Table structure for table `tb_kabupaten` */

DROP TABLE IF EXISTS `tb_kabupaten`;

CREATE TABLE `tb_kabupaten` (
  `id_kabupaten` int(11) NOT NULL AUTO_INCREMENT,
  `nm_kabupaten` varchar(50) DEFAULT NULL,
  `id_provinsi` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_kabupaten`),
  KEY `id_provinsi` (`id_provinsi`),
  CONSTRAINT `tb_kabupaten_ibfk_1` FOREIGN KEY (`id_provinsi`) REFERENCES `tb_provinsi` (`id_provinsi`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `tb_kabupaten` */

insert  into `tb_kabupaten`(`id_kabupaten`,`nm_kabupaten`,`id_provinsi`) values (1,'denpasar',1),(2,'bangli',1),(3,'tabanan',1),(4,'karangasem',1),(5,'jembrana',1),(6,'singaraja',1),(7,'gianyar',1),(8,'klungkung',1),(9,'badung',1),(10,'sempidi',1),(11,'test',2),(12,'tost',2),(13,'hai',2);

/*Table structure for table `tb_khs` */

DROP TABLE IF EXISTS `tb_khs`;

CREATE TABLE `tb_khs` (
  `id_khs` int(11) NOT NULL AUTO_INCREMENT,
  `id_semester` int(11) DEFAULT NULL,
  `id_mahasiswa` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_khs`),
  KEY `id_semester` (`id_semester`),
  KEY `id_mahasiswa` (`id_mahasiswa`),
  CONSTRAINT `tb_khs_ibfk_1` FOREIGN KEY (`id_semester`) REFERENCES `tb_semester` (`id_semester`),
  CONSTRAINT `tb_khs_ibfk_3` FOREIGN KEY (`id_mahasiswa`) REFERENCES `tb_mahasiswa` (`id_mahasiswa`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `tb_khs` */

insert  into `tb_khs`(`id_khs`,`id_semester`,`id_mahasiswa`) values (1,1,1),(2,2,1),(3,1,3),(4,1,2),(5,2,2),(6,2,3);

/*Table structure for table `tb_krs` */

DROP TABLE IF EXISTS `tb_krs`;

CREATE TABLE `tb_krs` (
  `id_krs` int(11) NOT NULL AUTO_INCREMENT,
  `id_semester` int(11) DEFAULT NULL,
  `id_mahasiswa` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_krs`),
  KEY `id_mahasiswa` (`id_mahasiswa`),
  KEY `id_semester` (`id_semester`),
  CONSTRAINT `tb_krs_ibfk_4` FOREIGN KEY (`id_mahasiswa`) REFERENCES `tb_mahasiswa` (`id_mahasiswa`),
  CONSTRAINT `tb_krs_ibfk_5` FOREIGN KEY (`id_semester`) REFERENCES `tb_semester` (`id_semester`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `tb_krs` */

insert  into `tb_krs`(`id_krs`,`id_semester`,`id_mahasiswa`) values (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,NULL,7),(8,NULL,8),(9,NULL,1),(10,NULL,2),(11,NULL,3),(12,NULL,4),(13,NULL,5),(14,NULL,6),(15,NULL,7),(16,NULL,8),(17,NULL,NULL),(18,NULL,NULL),(19,NULL,NULL),(20,NULL,NULL),(21,NULL,NULL),(22,NULL,NULL),(23,NULL,NULL),(24,NULL,NULL),(25,NULL,NULL),(26,NULL,NULL),(27,NULL,NULL),(28,NULL,NULL);

/*Table structure for table `tb_mahasiswa` */

DROP TABLE IF EXISTS `tb_mahasiswa`;

CREATE TABLE `tb_mahasiswa` (
  `id_mahasiswa` int(11) NOT NULL AUTO_INCREMENT,
  `NIM` varchar(11) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `alamat` varchar(50) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `tempat_lahir` varchar(50) DEFAULT NULL,
  `no_telp` varchar(13) DEFAULT NULL,
  `agama` varchar(20) DEFAULT NULL,
  `jenis_kelamin` enum('laki-laki','perempuan') DEFAULT NULL,
  `status_bekerja` enum('sudah_bekerja','belum_bekerja') DEFAULT NULL,
  `status_perkawinan` enum('sudah_kawin','belum_kawin') DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `id_kabupaten` int(11) DEFAULT NULL,
  `id_PA` int(11) DEFAULT NULL,
  `id_prodi` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_mahasiswa`),
  KEY `id_kabupaten` (`id_kabupaten`),
  KEY `id_PA` (`id_PA`),
  KEY `id_prodi` (`id_prodi`),
  CONSTRAINT `tb_mahasiswa_ibfk_1` FOREIGN KEY (`id_kabupaten`) REFERENCES `tb_kabupaten` (`id_kabupaten`),
  CONSTRAINT `tb_mahasiswa_ibfk_3` FOREIGN KEY (`id_PA`) REFERENCES `tb_pa` (`id_PA`),
  CONSTRAINT `tb_mahasiswa_ibfk_4` FOREIGN KEY (`id_prodi`) REFERENCES `tb_prodi` (`id_prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `tb_mahasiswa` */

insert  into `tb_mahasiswa`(`id_mahasiswa`,`NIM`,`nama`,`alamat`,`tgl_lahir`,`tempat_lahir`,`no_telp`,`agama`,`jenis_kelamin`,`status_bekerja`,`status_perkawinan`,`email`,`id_kabupaten`,`id_PA`,`id_prodi`) values (1,'1605551068','Ni Putu Ayu Widiari','denpasar','2018-11-14','denpasar','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','widiariayyu@gmail.com',1,1,1),(2,'1605551062','Laurensius Adi Kurniawan','denpasar','1997-10-25','melbourne','081237723316','katolik','laki-laki','belum_bekerja','belum_kawin','adikur62@gmail.com',5,2,2),(3,'1605551058','Praba Hridayami','denpasar','1997-12-10','mengwi','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','praba@gmail.com',2,1,4),(4,'1605551055','Ria Mandasari','mengwi','1998-07-15','badung','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','gek.ria@gmail.com',9,1,1),(5,'1605551068','Agastya Harta','jakarta','1998-08-10','tabanan','081237723316','hindu','laki-laki','belum_bekerja','belum_kawin','agash@gmail.com',3,1,1),(6,'1605551012','Yonatan ZT','badung','1998-05-23','denpasar','081237723316','kristen','laki-laki','belum_bekerja','belum_kawin','natanzt@gmail.com',4,1,5),(7,'1605551045','Savita','tabanan','1998-06-20','klungkung','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','savita.ajach@gmail.com',8,1,1),(8,'1605551070','Veggy','amerika','1998-04-12','gianyar','081237723316','hindu','perempuan','belum_bekerja','belum_kawin','veggy.h@gmail.com',7,1,1),(9,'1605551043','Trio Putra','london','1998-06-12','denpasar','081237723316','hindu','laki-laki','belum_bekerja','belum_kawin','trio@gmail.com',6,3,3),(10,'1605551082','Krisna Arynasta','denpasar','1998-06-13','denpasar','089765432111','hindu','laki-laki','belum_bekerja','belum_kawin','krisna@gmail.com',3,2,1),(11,'1605551078','tokek','deps','2018-12-08','denpasar','089777635267','hindu','laki-laki','belum_bekerja','belum_kawin','tick@gmail.com',3,4,1),(12,'1605551061','reyhan','deps','2018-12-08','denpasar','089765425268','hindu','laki-laki','belum_bekerja','belum_kawin','reyrey@gmail.com',2,4,1);

/*Table structure for table `tb_matkul` */

DROP TABLE IF EXISTS `tb_matkul`;

CREATE TABLE `tb_matkul` (
  `id_matkul` int(11) NOT NULL AUTO_INCREMENT,
  `kode_matkul` varchar(20) DEFAULT NULL,
  `nama_matkul` varchar(30) DEFAULT NULL,
  `sks` float DEFAULT NULL,
  PRIMARY KEY (`id_matkul`),
  KEY `id_matkul` (`id_matkul`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `tb_matkul` */

insert  into `tb_matkul`(`id_matkul`,`kode_matkul`,`nama_matkul`,`sks`) values (1,'C01','Computer Vision',3),(2,'D01','Datawarehouse',3),(3,'D02','Data Mining',3),(4,'I01','IOT',3),(5,'S01','STKI',3),(6,'T01','Teknologi Sensor Divais',3),(7,'E01','Etika Profesi dan Korupsi',3),(8,'R01','Rekayasa Perangkat Lunak',3),(9,'N01','Natural Language Processing',3),(10,'M01','Machine Learning',3),(11,'k01','test',2),(12,'k02','tost',3),(13,'k03','ticikk',3),(14,'k04','tokek',3),(15,'k05','puki',3),(16,'k06','colok',3),(17,'k07','puki',3),(18,'k08','plis',3),(19,'k09','maulah',3),(20,'k10','yoloh',3),(21,'k11','topai',2),(22,'k12','mau yaoloo',2);

/*Table structure for table `tb_pa` */

DROP TABLE IF EXISTS `tb_pa`;

CREATE TABLE `tb_pa` (
  `id_PA` int(11) NOT NULL AUTO_INCREMENT,
  `nama_PA` varchar(50) DEFAULT NULL,
  `alamat` varchar(50) DEFAULT NULL,
  `no_telp` char(12) DEFAULT NULL,
  PRIMARY KEY (`id_PA`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `tb_pa` */

insert  into `tb_pa`(`id_PA`,`nama_PA`,`alamat`,`no_telp`) values (1,'Agung Oka','denpasar','0897765478'),(2,'Agung Cahyawan','badung','0897665432'),(3,'Bayupati','denpasar','0832938282'),(4,'Suwija Putra','denpasar','0812938293'),(5,'Ayu Wirdiani','denpasar','0897654231'),(6,'I Kadek Gunawan','denpasar','0897654312'),(7,'praba hridayamin','denpasar','0897654352'),(8,'test','dps','0897654321'),(9,'coba','deps','0987653426'),(10,'tokek','deps','0897653425'),(11,'hai','tolol','08973892392'),(12,'tost','tolollll','08976368939'),(13,'tololl','hai','08543758904');

/*Table structure for table `tb_prodi` */

DROP TABLE IF EXISTS `tb_prodi`;

CREATE TABLE `tb_prodi` (
  `id_prodi` int(11) NOT NULL AUTO_INCREMENT,
  `nm_prodi` varchar(50) DEFAULT NULL,
  `id_fakultas` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_prodi`),
  KEY `id_fakultas` (`id_fakultas`),
  CONSTRAINT `tb_prodi_ibfk_1` FOREIGN KEY (`id_fakultas`) REFERENCES `tb_fakultas` (`id_fakultas`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `tb_prodi` */

insert  into `tb_prodi`(`id_prodi`,`nm_prodi`,`id_fakultas`) values (1,'teknologi informasi',1),(2,'teknik arsitektur',1),(3,'teknik sipil',1),(4,'teknik mesin',1),(5,'teknik elektro',2),(6,'kedokteran umum',2),(7,'kedokteran hewan',2),(8,'peternakan',1),(9,'tost',3),(10,'tisi',3),(11,'tiktok',2);

/*Table structure for table `tb_provinsi` */

DROP TABLE IF EXISTS `tb_provinsi`;

CREATE TABLE `tb_provinsi` (
  `id_provinsi` int(11) NOT NULL AUTO_INCREMENT,
  `nm_provinsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_provinsi`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `tb_provinsi` */

insert  into `tb_provinsi`(`id_provinsi`,`nm_provinsi`) values (1,'bali'),(2,'kalimantan utara'),(3,'kalimantan selatan'),(4,'tost'),(5,'tick'),(6,'prok');

/*Table structure for table `tb_semester` */

DROP TABLE IF EXISTS `tb_semester`;

CREATE TABLE `tb_semester` (
  `id_semester` int(11) NOT NULL AUTO_INCREMENT,
  `nama_semester` varchar(11) DEFAULT NULL,
  `tahun_ajaran` year(4) DEFAULT NULL,
  PRIMARY KEY (`id_semester`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `tb_semester` */

insert  into `tb_semester`(`id_semester`,`nama_semester`,`tahun_ajaran`) values (1,'Ganjil',2018),(2,'Genap',2018),(3,'Pendek',2018),(4,'Remidi',2018),(5,'test',2019),(6,'tost',2018);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
