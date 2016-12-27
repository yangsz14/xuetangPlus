-- MySQL dump 10.13  Distrib 5.7.11, for osx10.10 (x86_64)
--
-- Host: localhost    Database: xuetangplus_db2
-- ------------------------------------------------------
-- Server version	5.7.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user has course',7,'add_userhascourse'),(20,'Can change user has course',7,'change_userhascourse'),(21,'Can delete user has course',7,'delete_userhascourse'),(22,'Can add follow user',8,'add_followuser'),(23,'Can change follow user',8,'change_followuser'),(24,'Can delete follow user',8,'delete_followuser'),(25,'Can add bbs post',9,'add_bbspost'),(26,'Can change bbs post',9,'change_bbspost'),(27,'Can delete bbs post',9,'delete_bbspost'),(28,'Can add bbs course',10,'add_bbscourse'),(29,'Can change bbs course',10,'change_bbscourse'),(30,'Can delete bbs course',10,'delete_bbscourse'),(31,'Can add bbs user',11,'add_bbsuser'),(32,'Can change bbs user',11,'change_bbsuser'),(33,'Can delete bbs user',11,'delete_bbsuser'),(34,'Can add user like post',12,'add_userlikepost'),(35,'Can change user like post',12,'change_userlikepost'),(36,'Can delete user like post',12,'delete_userlikepost'),(37,'Can add user follow post',13,'add_userfollowpost'),(38,'Can change user follow post',13,'change_userfollowpost'),(39,'Can delete user follow post',13,'delete_userfollowpost'),(40,'Can add user has node',14,'add_userhasnode'),(41,'Can change user has node',14,'change_userhasnode'),(42,'Can delete user has node',14,'delete_userhasnode');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$S0cR90YmjH7k$T63/dsDmSNJqkRMT8zbOypckY26s7+XnSZOzh2670Eo=','2016-12-27 12:00:48.444615',1,'zzq','','','',1,1,'2016-12-07 17:03:09.715683'),(2,'pbkdf2_sha256$30000$rOR4t35UrLE8$rGyNoVPWDysMMxNeJ6JoTEdTTRSz12aV6oy6QKlTCdk=','2016-12-20 04:47:45.020350',0,'2014013458','','','',0,1,'2016-12-07 17:03:19.799979'),(3,'pbkdf2_sha256$30000$sjpMmsxYG3lz$LbSrqvXeKf/0LKej3FfOogMCzErlSqH5YOSALrTg9mU=','2016-12-27 08:17:33.468394',0,'2014013449','','','',0,1,'2016-12-07 17:05:34.123448');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-12-07 17:13:48.415815','1','2014013458',2,'[{\"changed\": {\"fields\": [\"U_Image\"]}}]',11,1),(2,'2016-12-18 16:52:46.449482','2','2014013449',2,'[{\"changed\": {\"fields\": [\"U_GPB\"]}}]',11,1),(3,'2016-12-18 17:04:34.228634','2','2014013449',2,'[{\"changed\": {\"fields\": [\"U_Level\", \"U_GPB\"]}}]',11,1),(4,'2016-12-18 17:12:48.475122','1','2014013458',2,'[]',11,1),(5,'2016-12-27 12:06:27.499252','95','鬼铠笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\", \"P_Level\"]}}]',9,1),(6,'2016-12-27 12:06:33.349439','96','次元突破笔记',2,'[{\"changed\": {\"fields\": [\"P_Level\"]}}]',9,1),(7,'2016-12-27 12:06:38.140190','97','月光笔记',2,'[{\"changed\": {\"fields\": [\"P_Level\"]}}]',9,1),(8,'2016-12-27 12:06:42.068007','98','白练笔记',2,'[{\"changed\": {\"fields\": [\"P_Level\"]}}]',9,1),(9,'2016-12-27 12:06:46.833666','99','强袭笔记',2,'[]',9,1),(10,'2016-12-27 12:06:54.259859','100','影舞冲击笔记',2,'[]',9,1),(11,'2016-12-27 12:07:01.929867','95','鬼铠笔记',2,'[]',9,1),(12,'2016-12-27 12:07:06.883320','96','次元突破笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\"]}}]',9,1),(13,'2016-12-27 12:07:25.353947','97','月光笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\"]}}]',9,1),(14,'2016-12-27 12:07:28.176280','96','次元突破笔记',2,'[]',9,1),(15,'2016-12-27 12:07:33.023083','98','白练笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\"]}}]',9,1),(16,'2016-12-27 12:07:38.169529','99','强袭笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\"]}}]',9,1),(17,'2016-12-27 12:07:42.399209','100','影舞冲击笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\"]}}]',9,1),(18,'2016-12-27 12:07:49.440251','101','圣女祈祷笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\", \"P_Level\"]}}]',9,1),(19,'2016-12-27 12:07:59.802042','101','圣女祈祷笔记',2,'[]',9,1),(20,'2016-12-27 12:08:15.257065','102','绯红笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\", \"P_Level\"]}}]',9,1),(21,'2016-12-27 12:08:19.979500','102','绯红笔记',2,'[{\"changed\": {\"fields\": [\"P_Level\"]}}]',9,1),(22,'2016-12-27 12:08:25.028327','103','山吹笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\", \"P_Level\"]}}]',9,1),(23,'2016-12-27 12:08:30.132377','104','雪地狙击笔记',2,'[{\"changed\": {\"fields\": [\"P_Type\", \"P_Level\"]}}]',9,1),(24,'2016-12-27 12:53:41.692635','2','2014013449',2,'[{\"changed\": {\"fields\": [\"U_Image\"]}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(2,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(10,'web','bbscourse'),(9,'web','bbspost'),(11,'web','bbsuser'),(8,'web','followuser'),(13,'web','userfollowpost'),(7,'web','userhascourse'),(14,'web','userhasnode'),(12,'web','userlikepost');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-12-07 17:02:48.014286'),(2,'auth','0001_initial','2016-12-07 17:02:48.343245'),(3,'admin','0001_initial','2016-12-07 17:02:48.411307'),(4,'admin','0002_logentry_remove_auto_add','2016-12-07 17:02:48.463123'),(5,'contenttypes','0002_remove_content_type_name','2016-12-07 17:02:48.524554'),(6,'auth','0002_alter_permission_name_max_length','2016-12-07 17:02:48.553527'),(7,'auth','0003_alter_user_email_max_length','2016-12-07 17:02:48.580665'),(8,'auth','0004_alter_user_username_opts','2016-12-07 17:02:48.591998'),(9,'auth','0005_alter_user_last_login_null','2016-12-07 17:02:48.619268'),(10,'auth','0006_require_contenttypes_0002','2016-12-07 17:02:48.620609'),(11,'auth','0007_alter_validators_add_error_messages','2016-12-07 17:02:48.628850'),(12,'auth','0008_alter_user_username_max_length','2016-12-07 17:02:48.655515'),(13,'sessions','0001_initial','2016-12-07 17:02:48.695686'),(14,'web','0001_initial','2016-12-07 17:02:49.173922'),(15,'web','0002_bbspost_p_wanted','2016-12-17 16:10:50.284015'),(16,'web','0003_auto_20161218_0159','2016-12-17 17:59:19.877144'),(17,'web','0004_bbsuser_u_honor','2016-12-18 16:55:36.828832'),(18,'web','0005_userhasnode','2016-12-27 08:19:57.250653'),(19,'web','0006_bbspost_p_level','2016-12-27 11:32:52.808829');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gi056unyytyvit4u48ro9kqn2rh9rdlu','MGQ0YzYwMzQzYzhhYmExMmJkY2FiMzYyNjQyMWNlZWEwMTI4ZmVhYTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWExNTRjZGEyZGNiNzdhMDY4ZmJlMDI0YjZiNzhkMDc2MjlkMjc2MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-01-03 04:47:45.022067'),('hzq7lgi7wou7dk8fw5h8dngooovilj99','YmI3NmMxODJlMjY5NzIzNjFmOGM1ZjI1NWI4MGVlZWI1OWY0ZWU3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjRmODNkOTU0ZWQzYmY4ZGQzNGRkNDcwMWIzMmVmYjlkY2RjOTE5NGYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-01-10 12:00:48.447420');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_bbscourse`
--

DROP TABLE IF EXISTS `web_bbscourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_bbscourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `C_Name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `C_SeqNum` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_bbscourse`
--

LOCK TABLES `web_bbscourse` WRITE;
/*!40000 ALTER TABLE `web_bbscourse` DISABLE KEYS */;
INSERT INTO `web_bbscourse` VALUES (1,'三年级男生功夫扇','2016-2017-1-10721341-2'),(2,'计算机与网络体系结构(1)','2016-2017-1-34100294-0'),(3,'软件工程（3）','2016-2017-1-34100325-0'),(4,'计算机与网络体系结构（2）','2016-2017-1-34100344-0'),(5,'软件理论基础(2):函数式语言程序设计','2016-2017-1-34100352-0'),(6,'环境保护与可持续发展','2016-2017-1-00050071-90'),(7,'大学生音乐知识与欣赏','2016-2017-1-00780091-90'),(8,'多元文化中的音乐现象','2016-2017-1-00781882-90'),(9,'外国工艺美术史','2016-2017-1-00800042-90'),(10,'三年级男生网球','2016-2017-1-10721041-12');
/*!40000 ALTER TABLE `web_bbscourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_bbspost`
--

DROP TABLE IF EXISTS `web_bbspost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_bbspost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `P_Type` int(11) NOT NULL,
  `P_Title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `P_Content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `P_Time` datetime(6) NOT NULL,
  `P_LastComTime` datetime(6) NOT NULL,
  `P_LikeNum` int(11) NOT NULL,
  `P_Section` int(11) NOT NULL,
  `P_ReplyNum` int(11) NOT NULL,
  `P_Top` int(11) NOT NULL,
  `P_Course_id` int(11) NOT NULL,
  `P_Parent_id` int(11) DEFAULT NULL,
  `P_User_id` int(11) NOT NULL,
  `P_Wanted` int(11) NOT NULL,
  `P_BestChild_id` int(11) DEFAULT NULL,
  `P_Level` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_bbspost_P_Course_id_6173fade_fk_web_bbscourse_id` (`P_Course_id`),
  KEY `web_bbspost_01d48799` (`P_User_id`),
  KEY `web_bbspost_P_Parent_id_7711709a_fk_web_bbspost_id` (`P_Parent_id`),
  KEY `web_bbspost_8d4e3b11` (`P_BestChild_id`),
  CONSTRAINT `web_bbspost_P_BestChild_id_b081df58_fk_web_bbspost_id` FOREIGN KEY (`P_BestChild_id`) REFERENCES `web_bbspost` (`id`),
  CONSTRAINT `web_bbspost_P_Course_id_6173fade_fk_web_bbscourse_id` FOREIGN KEY (`P_Course_id`) REFERENCES `web_bbscourse` (`id`),
  CONSTRAINT `web_bbspost_P_Parent_id_7711709a_fk_web_bbspost_id` FOREIGN KEY (`P_Parent_id`) REFERENCES `web_bbspost` (`id`),
  CONSTRAINT `web_bbspost_P_User_id_2eb5c6aa_fk_web_bbsuser_id` FOREIGN KEY (`P_User_id`) REFERENCES `web_bbsuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_bbspost`
--

LOCK TABLES `web_bbspost` WRITE;
/*!40000 ALTER TABLE `web_bbspost` DISABLE KEYS */;
INSERT INTO `web_bbspost` VALUES (3,0,'28374g','f3','2016-12-07 17:13:14.462965','2016-12-07 17:13:14.462977',2,1,0,0,3,NULL,1,0,NULL,0),(4,3,'2134','123','2016-12-07 17:19:48.847147','2016-12-07 17:19:48.847154',0,1,0,0,3,3,1,0,NULL,0),(8,3,'1','2','2016-12-07 17:39:11.508414','2016-12-07 17:39:11.508422',0,1,0,0,3,3,1,0,NULL,0),(9,0,'测试','这是一条测试贴','2016-12-14 11:53:29.934235','2016-12-14 11:53:29.934246',0,1,0,0,3,NULL,1,0,NULL,0),(10,3,'回复测试','这是一条测试回复帖','2016-12-14 11:54:06.942609','2016-12-14 11:54:06.942617',0,1,0,0,3,9,1,0,NULL,0),(13,4,'公告测试4','公告测试4内容','2016-12-14 13:03:59.212885','2016-12-14 13:03:59.212896',0,0,0,0,1,NULL,1,0,NULL,0),(19,0,'Haskell','Haskell233','2016-12-14 14:04:29.250271','2016-12-14 14:04:29.250283',0,1,0,0,5,NULL,1,0,NULL,0),(39,4,'666','233','2016-12-17 13:48:33.409444','2016-12-17 13:48:33.409451',0,1,0,0,1,13,2,0,NULL,0),(40,0,'测试','测试美术史','2016-12-17 13:56:16.457110','2016-12-17 13:56:16.457124',0,1,0,0,9,NULL,2,0,NULL,0),(41,4,'日语课','日语难','2016-12-17 13:56:40.542135','2016-12-17 13:56:40.542146',1,9,0,0,1,NULL,2,0,NULL,0),(42,3,'','回复','2016-12-17 15:41:06.998930','2016-12-17 15:41:06.998937',0,1,0,0,9,40,2,0,NULL,0),(71,0,'gpb','gpb','2016-12-18 16:44:01.629224','2016-12-18 16:44:01.629234',1,1,0,0,3,NULL,2,0,NULL,0),(72,0,'1111','2','2016-12-18 16:44:59.091701','2016-12-18 16:44:59.091710',0,1,0,0,3,NULL,2,0,NULL,0),(73,4,'1','2','2016-12-18 16:46:11.257954','2016-12-18 16:46:11.257967',0,0,0,0,1,NULL,2,0,NULL,0),(74,4,'1','2','2016-12-18 16:46:12.321500','2016-12-18 16:46:12.321510',0,0,0,0,1,NULL,2,0,NULL,0),(75,4,'1','2','2016-12-18 16:46:15.368336','2016-12-18 16:46:15.368348',0,0,0,0,1,NULL,2,0,NULL,0),(76,4,'43','54','2016-12-18 16:46:21.313625','2016-12-18 16:46:21.313636',0,0,0,0,1,NULL,2,0,NULL,0),(77,4,'1','2','2016-12-18 16:47:26.164313','2016-12-18 16:47:26.164328',0,0,0,0,1,NULL,2,0,NULL,0),(78,4,'1','2','2016-12-18 16:47:53.617962','2016-12-18 16:47:53.617976',1,0,0,0,1,NULL,2,0,NULL,0),(84,4,'56','32','2016-12-18 17:05:05.564724','2016-12-18 17:05:05.564734',0,5,0,0,1,NULL,2,0,NULL,0),(85,4,'3f','efw','2016-12-18 17:05:13.700944','2016-12-18 17:05:13.700954',0,7,0,0,1,NULL,2,0,NULL,0),(88,1,'233','666','2016-12-18 17:37:43.349012','2016-12-18 17:37:43.349022',0,1,0,0,6,NULL,2,20,NULL,0),(89,3,'回复','555','2016-12-18 17:37:47.558862','2016-12-18 17:37:47.558869',0,1,0,0,6,88,2,0,NULL,0),(93,3,'回复','666','2016-12-18 17:44:51.133877','2016-12-18 17:44:51.133884',0,1,0,0,6,88,2,0,NULL,0),(94,3,'回复','777','2016-12-18 17:47:47.695785','2016-12-18 17:47:47.695792',0,1,0,0,6,88,2,0,NULL,0),(95,2,'鬼铠笔记','鬼铠笔记','2016-12-27 12:02:29.000000','2016-12-27 12:02:29.000000',0,1,0,0,1,NULL,1,0,NULL,2),(96,2,'次元突破笔记','次元突破','2016-12-27 12:02:53.000000','2016-12-27 12:02:53.000000',0,1,0,0,1,NULL,1,0,NULL,1),(97,2,'月光笔记','月光','2016-12-27 12:03:01.000000','2016-12-27 12:03:01.000000',0,1,0,0,1,NULL,1,0,NULL,2),(98,2,'白练笔记','白练','2016-12-27 12:03:12.000000','2016-12-27 12:03:12.000000',0,1,0,0,1,NULL,1,0,NULL,1),(99,2,'强袭笔记','强袭','2016-12-27 12:03:29.000000','2016-12-27 12:03:29.000000',0,1,0,0,1,NULL,1,0,NULL,0),(100,2,'影舞冲击笔记','影舞冲击','2016-12-27 12:03:41.000000','2016-12-27 12:03:41.000000',0,1,0,0,1,NULL,1,0,NULL,0),(101,2,'圣女祈祷笔记','圣女祈祷','2016-12-27 12:03:55.000000','2016-12-27 12:03:55.000000',0,1,0,0,1,NULL,1,0,NULL,1),(102,2,'绯红笔记','绯红','2016-12-27 12:04:12.000000','2016-12-27 12:04:12.000000',0,1,0,0,1,NULL,1,0,NULL,0),(103,2,'山吹笔记','山吹','2016-12-27 12:04:23.000000','2016-12-27 12:04:23.000000',0,1,0,0,1,NULL,1,0,NULL,1),(104,2,'雪地狙击笔记','雪地狙击','2016-12-27 12:04:35.000000','2016-12-27 12:04:35.000000',0,1,0,0,1,NULL,1,0,NULL,1),(110,3,'回复','100','2016-12-27 13:19:22.391495','2016-12-27 13:19:22.391503',0,1,0,0,1,13,1,0,NULL,0),(111,3,'回复','100','2016-12-27 13:37:01.165571','2016-12-27 13:37:01.165593',0,1,0,0,1,13,1,0,NULL,0),(112,3,'回复','100','2016-12-27 13:37:03.684701','2016-12-27 13:37:03.684752',0,1,0,0,1,13,1,0,NULL,0);
/*!40000 ALTER TABLE `web_bbspost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_bbsuser`
--

DROP TABLE IF EXISTS `web_bbsuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_bbsuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `U_studentid` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `U_password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `U_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `U_RealName` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `U_Major` longtext COLLATE utf8_unicode_ci NOT NULL,
  `U_Description` longtext COLLATE utf8_unicode_ci,
  `U_Image` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `U_Identity` int(11) NOT NULL,
  `U_Level` int(11) NOT NULL,
  `U_GPB` int(11) NOT NULL,
  `U_FollowUserNum` int(11) NOT NULL,
  `U_FollowPostNum` int(11) NOT NULL,
  `U_PostNum` int(11) NOT NULL,
  `U_QuestionNum` int(11) NOT NULL,
  `U_AnswerNum` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `U_Honor` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `web_bbsuser_user_id_04995852_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_bbsuser`
--

LOCK TABLES `web_bbsuser` WRITE;
/*!40000 ALTER TABLE `web_bbsuser` DISABLE KEYS */;
INSERT INTO `web_bbsuser` VALUES (1,'2014013458','','','张智晴','软件学院','','13944118.jpeg',1,128,2530,0,0,0,0,0,2,'超絶かわいい'),(2,'2014013449','','','杨松臻','软件学院','','ham002009.png',1,33,-580,0,0,0,0,0,3,'咕咕咕');
/*!40000 ALTER TABLE `web_bbsuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_followuser`
--

DROP TABLE IF EXISTS `web_followuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_followuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `User1ID_id` int(11) NOT NULL,
  `User2ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_followuser_User1ID_id_6cae6afd_fk_web_bbsuser_id` (`User1ID_id`),
  KEY `web_followuser_User2ID_id_7206420e_fk_auth_user_id` (`User2ID_id`),
  CONSTRAINT `web_followuser_User1ID_id_6cae6afd_fk_web_bbsuser_id` FOREIGN KEY (`User1ID_id`) REFERENCES `web_bbsuser` (`id`),
  CONSTRAINT `web_followuser_User2ID_id_7206420e_fk_auth_user_id` FOREIGN KEY (`User2ID_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_followuser`
--

LOCK TABLES `web_followuser` WRITE;
/*!40000 ALTER TABLE `web_followuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `web_followuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_userfollowpost`
--

DROP TABLE IF EXISTS `web_userfollowpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_userfollowpost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `PostID_id` int(11) NOT NULL,
  `UserID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_userfollowpost_PostID_id_e73df2b0_fk_web_bbspost_id` (`PostID_id`),
  KEY `web_userfollowpost_UserID_id_e2501853_fk_web_bbsuser_id` (`UserID_id`),
  CONSTRAINT `web_userfollowpost_PostID_id_e73df2b0_fk_web_bbspost_id` FOREIGN KEY (`PostID_id`) REFERENCES `web_bbspost` (`id`),
  CONSTRAINT `web_userfollowpost_UserID_id_e2501853_fk_web_bbsuser_id` FOREIGN KEY (`UserID_id`) REFERENCES `web_bbsuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_userfollowpost`
--

LOCK TABLES `web_userfollowpost` WRITE;
/*!40000 ALTER TABLE `web_userfollowpost` DISABLE KEYS */;
/*!40000 ALTER TABLE `web_userfollowpost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_userhascourse`
--

DROP TABLE IF EXISTS `web_userhascourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_userhascourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `CourseID_id` int(11) NOT NULL,
  `UserID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_userhascourse_CourseID_id_506aadc7_fk_web_bbscourse_id` (`CourseID_id`),
  KEY `web_userhascourse_UserID_id_49e5c833_fk_web_bbsuser_id` (`UserID_id`),
  CONSTRAINT `web_userhascourse_CourseID_id_506aadc7_fk_web_bbscourse_id` FOREIGN KEY (`CourseID_id`) REFERENCES `web_bbscourse` (`id`),
  CONSTRAINT `web_userhascourse_UserID_id_49e5c833_fk_web_bbsuser_id` FOREIGN KEY (`UserID_id`) REFERENCES `web_bbsuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_userhascourse`
--

LOCK TABLES `web_userhascourse` WRITE;
/*!40000 ALTER TABLE `web_userhascourse` DISABLE KEYS */;
INSERT INTO `web_userhascourse` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,2),(7,7,2),(8,8,2),(9,9,2),(10,10,2),(11,2,2),(12,3,2),(13,4,2),(14,5,2);
/*!40000 ALTER TABLE `web_userhascourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_userhasnode`
--

DROP TABLE IF EXISTS `web_userhasnode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_userhasnode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `PostID_id` int(11) NOT NULL,
  `UserID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_userhasnode_PostID_id_541498e9_fk_web_bbspost_id` (`PostID_id`),
  KEY `web_userhasnode_UserID_id_1371490f_fk_web_bbsuser_id` (`UserID_id`),
  CONSTRAINT `web_userhasnode_PostID_id_541498e9_fk_web_bbspost_id` FOREIGN KEY (`PostID_id`) REFERENCES `web_bbspost` (`id`),
  CONSTRAINT `web_userhasnode_UserID_id_1371490f_fk_web_bbsuser_id` FOREIGN KEY (`UserID_id`) REFERENCES `web_bbsuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_userhasnode`
--

LOCK TABLES `web_userhasnode` WRITE;
/*!40000 ALTER TABLE `web_userhasnode` DISABLE KEYS */;
/*!40000 ALTER TABLE `web_userhasnode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_userlikepost`
--

DROP TABLE IF EXISTS `web_userlikepost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_userlikepost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `PostID_id` int(11) NOT NULL,
  `UserID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_userlikepost_PostID_id_67c9eb49_fk_web_bbspost_id` (`PostID_id`),
  KEY `web_userlikepost_UserID_id_e545ac31_fk_web_bbsuser_id` (`UserID_id`),
  CONSTRAINT `web_userlikepost_PostID_id_67c9eb49_fk_web_bbspost_id` FOREIGN KEY (`PostID_id`) REFERENCES `web_bbspost` (`id`),
  CONSTRAINT `web_userlikepost_UserID_id_e545ac31_fk_web_bbsuser_id` FOREIGN KEY (`UserID_id`) REFERENCES `web_bbsuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_userlikepost`
--

LOCK TABLES `web_userlikepost` WRITE;
/*!40000 ALTER TABLE `web_userlikepost` DISABLE KEYS */;
INSERT INTO `web_userlikepost` VALUES (8,3,1),(12,41,1),(13,3,2),(14,78,2),(15,71,2);
/*!40000 ALTER TABLE `web_userlikepost` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-27 21:43:48
