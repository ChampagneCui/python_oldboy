-- MySQL dump 10.13  Distrib 5.6.33, for Win64 (x86_64)
--
-- Host: localhost    Database: cmdb
-- ------------------------------------------------------
-- Server version	5.6.33

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
-- Table structure for table `account_account`
--

DROP TABLE IF EXISTS `account_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(32) NOT NULL,
  `avatar` varchar(300) DEFAULT NULL,
  `cust_id` int(11) DEFAULT NULL,
  `username_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_id` (`username_id`),
  KEY `account_account_cust_id_6b99a776_fk` (`cust_id`),
  CONSTRAINT `account_account_cust_id_6b99a776_fk` FOREIGN KEY (`cust_id`) REFERENCES `cmdb_basecustomerinfo` (`idcode`),
  CONSTRAINT `account_account_username_id_be2499ec_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_account`
--

LOCK TABLES `account_account` WRITE;
/*!40000 ALTER TABLE `account_account` DISABLE KEYS */;
INSERT INTO `account_account` VALUES (1,'cmdb','default.jpg',1001,3),(2,'cmdb_test','default.jpg',1001,5),(3,'测试1','default.jpg',1001,6),(4,'Administrator','default.jpg',1001,7);
/*!40000 ALTER TABLE `account_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_menus`
--

DROP TABLE IF EXISTS `account_menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_menus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_code` varchar(100) NOT NULL,
  `menu_name` varchar(200) NOT NULL,
  `is_avaible` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100119 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_menus`
--

LOCK TABLES `account_menus` WRITE;
/*!40000 ALTER TABLE `account_menus` DISABLE KEYS */;
INSERT INTO `account_menus` VALUES (10011,'m_001_0','计算',0),(10012,'m_002_0','网络',0),(10013,'m_003_0','存储',0),(10014,'m_004_0','安全',0),(10015,'m_005_0','容器',0),(10016,'m_006_0','监控',1),(10017,'m_007_0','CMDB',1),(10018,'m_008_0','自动化运维',0),(10019,'m_009_0','服务编排',0),(100110,'m_010_0','高可用',0),(100111,'m_011_0','业务性能分析',0),(100112,'m_012_0','微服务',0),(100113,'m_013_0','大数据',0),(100114,'m_014_0','日志',0),(100115,'m_015_0','邮件',0),(100116,'m_016_0','知识库',1),(100117,'m_017_0','应用市场',0),(100118,'m_018_0','帐号管理',1);
/*!40000 ALTER TABLE `account_menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'cmdbgroup');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=929 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user object permission',7,'add_userobjectpermission'),(20,'Can change user object permission',7,'change_userobjectpermission'),(21,'Can delete user object permission',7,'delete_userobjectpermission'),(22,'Can add group object permission',8,'add_groupobjectpermission'),(23,'Can change group object permission',8,'change_groupobjectpermission'),(24,'Can delete group object permission',8,'delete_groupobjectpermission'),(25,'Can add asset history',9,'add_assethistory'),(26,'Can change asset history',9,'change_assethistory'),(27,'Can delete asset history',9,'delete_assethistory'),(28,'can view AssetHistory Record',9,'view_assethistory'),(29,'Can add ids',10,'add_ids'),(30,'Can change ids',10,'change_ids'),(31,'Can delete ids',10,'delete_ids'),(32,'can view ids',10,'view_ids'),(33,'Can add 审计',11,'add_operateaudit'),(34,'Can change 审计',11,'change_operateaudit'),(35,'Can delete 审计',11,'delete_operateaudit'),(36,'can view OperateAudit',11,'view_operateaudit'),(37,'Can add port mapping',12,'add_portmapping'),(38,'Can change port mapping',12,'change_portmapping'),(39,'Can delete port mapping',12,'delete_portmapping'),(40,'Can add port list',13,'add_portlist'),(41,'Can change port list',13,'change_portlist'),(42,'Can delete port list',13,'delete_portlist'),(43,'Can add 软件分类',14,'add_basesofttype'),(44,'Can change 软件分类',14,'change_basesofttype'),(45,'Can delete 软件分类',14,'delete_basesofttype'),(46,'can view BaseSoftType',14,'view_basesofttype'),(47,'Can add 联系人',15,'add_staffs'),(48,'Can change 联系人',15,'change_staffs'),(49,'Can delete 联系人',15,'delete_staffs'),(50,'Can View Staffs',15,'view_staffs'),(51,'Can add 软件列表',16,'add_basesoft'),(52,'Can change 软件列表',16,'change_basesoft'),(53,'Can delete 软件列表',16,'delete_basesoft'),(54,'can view BaseSoft',16,'view_basesoft'),(55,'Can add 软件Lisence',17,'add_softlisence'),(56,'Can change 软件Lisence',17,'change_softlisence'),(57,'Can delete 软件Lisence',17,'delete_softlisence'),(58,'can view SoftLisence',17,'view_softlisence'),(59,'Can add storage pv',18,'add_storagepv'),(60,'Can change storage pv',18,'change_storagepv'),(61,'Can delete storage pv',18,'delete_storagepv'),(62,'Can add servers',19,'add_servers'),(63,'Can change servers',19,'change_servers'),(64,'Can delete servers',19,'delete_servers'),(65,'Can View Servers',19,'view_servers'),(66,'Can add 机柜',20,'add_baseassetcabinet'),(67,'Can change 机柜',20,'change_baseassetcabinet'),(68,'Can delete 机柜',20,'delete_baseassetcabinet'),(69,'can view BaseAssetCabinet',20,'view_baseassetcabinet'),(70,'Can add 设备厂商',21,'add_basefactory'),(71,'Can change 设备厂商',21,'change_basefactory'),(72,'Can delete 设备厂商',21,'delete_basefactory'),(73,'can view BaseFactory',21,'view_basefactory'),(74,'Can add r_ server_ staff',22,'add_r_server_staff'),(75,'Can change r_ server_ staff',22,'change_r_server_staff'),(76,'Can delete r_ server_ staff',22,'delete_r_server_staff'),(77,'Can add cpu memory',23,'add_cpumemory'),(78,'Can change cpu memory',23,'change_cpumemory'),(79,'Can delete cpu memory',23,'delete_cpumemory'),(80,'Can add server board card',24,'add_serverboardcard'),(81,'Can change server board card',24,'change_serverboardcard'),(82,'Can delete server board card',24,'delete_serverboardcard'),(83,'Can add ip source',25,'add_ipsource'),(84,'Can change ip source',25,'change_ipsource'),(85,'Can delete ip source',25,'delete_ipsource'),(86,'Can View IPSource',25,'view_ipsource'),(87,'Can add 公司基表',26,'add_basecompany'),(88,'Can change 公司基表',26,'change_basecompany'),(89,'Can delete 公司基表',26,'delete_basecompany'),(90,'can view BaseCompany',26,'view_basecompany'),(91,'Can add installed soft list',27,'add_installedsoftlist'),(92,'Can change installed soft list',27,'change_installedsoftlist'),(93,'Can delete installed soft list',27,'delete_installedsoftlist'),(94,'Can add equipment board card',28,'add_equipmentboardcard'),(95,'Can change equipment board card',28,'change_equipmentboardcard'),(96,'Can delete equipment board card',28,'delete_equipmentboardcard'),(97,'Can add 机房',29,'add_basemachineroom'),(98,'Can change 机房',29,'change_basemachineroom'),(99,'Can delete 机房',29,'delete_basemachineroom'),(100,'can view BaseMachineRoom',29,'view_basemachineroom'),(101,'Can add 网络区域',30,'add_basenetarea'),(102,'Can change 网络区域',30,'change_basenetarea'),(103,'Can delete 网络区域',30,'delete_basenetarea'),(104,'can view BaseNetArea',30,'view_basenetarea'),(105,'Can add 运行状态',31,'add_baserunningstatus'),(106,'Can change 运行状态',31,'change_baserunningstatus'),(107,'Can delete 运行状态',31,'delete_baserunningstatus'),(108,'can view RunningStatus',31,'view baserunningstatus'),(109,'Can add r_ machine room_ staff',32,'add_r_machineroom_staff'),(110,'Can change r_ machine room_ staff',32,'change_r_machineroom_staff'),(111,'Can delete r_ machine room_ staff',32,'delete_r_machineroom_staff'),(112,'Can add storage vg',33,'add_storagevg'),(113,'Can change storage vg',33,'change_storagevg'),(114,'Can delete storage vg',33,'delete_storagevg'),(115,'Can add r_ project_ staff',34,'add_r_project_staff'),(116,'Can change r_ project_ staff',34,'change_r_project_staff'),(117,'Can delete r_ project_ staff',34,'delete_r_project_staff'),(118,'Can add 设备状态',35,'add_baseassetstatus'),(119,'Can change 设备状态',35,'change_baseassetstatus'),(120,'Can delete 设备状态',35,'delete_baseassetstatus'),(121,'can view BaseAssetStatus',35,'view_baseassetstatus'),(122,'Can add ip configuration',36,'add_ipconfiguration'),(123,'Can change ip configuration',36,'change_ipconfiguration'),(124,'Can delete ip configuration',36,'delete_ipconfiguration'),(125,'Can add storage lv',37,'add_storagelv'),(126,'Can change storage lv',37,'change_storagelv'),(127,'Can delete storage lv',37,'delete_storagelv'),(128,'Can add 网络设备类型',38,'add_baseequipmenttype'),(129,'Can change 网络设备类型',38,'change_baseequipmenttype'),(130,'Can delete 网络设备类型',38,'delete_baseequipmenttype'),(131,'Can View BaseEquipmentType',38,'view_baseequipmenttype'),(132,'Can add 服务器类型',39,'add_baseassettype'),(133,'Can change 服务器类型',39,'change_baseassettype'),(134,'Can delete 服务器类型',39,'delete_baseassettype'),(135,'can view BaseAssetType',39,'view_baseassettype'),(136,'Can add 角色表',40,'add_baserole'),(137,'Can change 角色表',40,'change_baserole'),(138,'Can delete 角色表',40,'delete_baserole'),(139,'can view BaseRole',40,'view_baserole'),(140,'Can add 主机子类型',41,'add_baseassetsubtype'),(141,'Can change 主机子类型',41,'change_baseassetsubtype'),(142,'Can delete 主机子类型',41,'delete_baseassetsubtype'),(143,'can view BaseAssetSubtype',41,'view_baseassetsubtype'),(144,'Can add 客户信息表',42,'add_basecustomerinfo'),(145,'Can change 客户信息表',42,'change_basecustomerinfo'),(146,'Can delete 客户信息表',42,'delete_basecustomerinfo'),(147,'can view BaseCustomerInfo',42,'view_basecustomerinfo'),(148,'Can add r_ server_ business',43,'add_r_server_business'),(149,'Can change r_ server_ business',43,'change_r_server_business'),(150,'Can delete r_ server_ business',43,'delete_r_server_business'),(151,'Can add equipment',44,'add_equipment'),(152,'Can change equipment',44,'change_equipment'),(153,'Can delete equipment',44,'delete_equipment'),(154,'Can View Equipment',44,'view_equipment'),(155,'Can add assets',45,'add_assets'),(156,'Can change assets',45,'change_assets'),(157,'Can delete assets',45,'delete_assets'),(158,'Can View Assets',45,'view_assets'),(159,'Can add 数据中心',46,'add_basedatacenter'),(160,'Can change 数据中心',46,'change_basedatacenter'),(161,'Can delete 数据中心',46,'delete_basedatacenter'),(162,'can view BaseDataCenter',46,'view_basedatacenter'),(163,'Can add RAID类型',47,'add_baseraidtype'),(164,'Can change RAID类型',47,'change_baseraidtype'),(165,'Can delete RAID类型',47,'delete_baseraidtype'),(166,'can view BaseRaidType',47,'view_baseraidtype'),(167,'Can add r_ equipment_ staff',48,'add_r_equipment_staff'),(168,'Can change r_ equipment_ staff',48,'change_r_equipment_staff'),(169,'Can delete r_ equipment_ staff',48,'delete_r_equipment_staff'),(170,'Can add ip allocation',49,'add_ipallocation'),(171,'Can change ip allocation',49,'change_ipallocation'),(172,'Can delete ip allocation',49,'delete_ipallocation'),(173,'Can View IPAllocation',49,'view_ipallocation'),(174,'Can add 业务模块',50,'add_business'),(175,'Can change 业务模块',50,'change_business'),(176,'Can delete 业务模块',50,'delete_business'),(177,'Can View Business',50,'view_business'),(178,'Can add 部门基表',51,'add_basedepartment'),(179,'Can change 部门基表',51,'change_basedepartment'),(180,'Can delete 部门基表',51,'delete_basedepartment'),(181,'can view BaseDepartment',51,'view_basedepartment'),(182,'Can add 项目信息',52,'add_projects'),(183,'Can change 项目信息',52,'change_projects'),(184,'Can delete 项目信息',52,'delete_projects'),(185,'Can View Projects',52,'view_projects'),(186,'Can add acknowledges',53,'add_acknowledges'),(187,'Can change acknowledges',53,'change_acknowledges'),(188,'Can delete acknowledges',53,'delete_acknowledges'),(189,'Can add actions',54,'add_actions'),(190,'Can change actions',54,'change_actions'),(191,'Can delete actions',54,'delete_actions'),(192,'Can add alerts',55,'add_alerts'),(193,'Can change alerts',55,'change_alerts'),(194,'Can delete alerts',55,'delete_alerts'),(195,'Can add application discovery',56,'add_applicationdiscovery'),(196,'Can change application discovery',56,'change_applicationdiscovery'),(197,'Can delete application discovery',56,'delete_applicationdiscovery'),(198,'Can add application prototype',57,'add_applicationprototype'),(199,'Can change application prototype',57,'change_applicationprototype'),(200,'Can delete application prototype',57,'delete_applicationprototype'),(201,'Can add applications',58,'add_applications'),(202,'Can change applications',58,'change_applications'),(203,'Can delete applications',58,'delete_applications'),(204,'Can add application template',59,'add_applicationtemplate'),(205,'Can change application template',59,'change_applicationtemplate'),(206,'Can delete application template',59,'delete_applicationtemplate'),(207,'Can add auditlog',60,'add_auditlog'),(208,'Can change auditlog',60,'change_auditlog'),(209,'Can delete auditlog',60,'delete_auditlog'),(210,'Can add auditlog details',61,'add_auditlogdetails'),(211,'Can change auditlog details',61,'change_auditlogdetails'),(212,'Can delete auditlog details',61,'delete_auditlogdetails'),(213,'Can add autoreg host',62,'add_autoreghost'),(214,'Can change autoreg host',62,'change_autoreghost'),(215,'Can delete autoreg host',62,'delete_autoreghost'),(216,'Can add conditions',63,'add_conditions'),(217,'Can change conditions',63,'change_conditions'),(218,'Can delete conditions',63,'delete_conditions'),(219,'Can add config',64,'add_config'),(220,'Can change config',64,'change_config'),(221,'Can delete config',64,'delete_config'),(222,'Can add dbversion',65,'add_dbversion'),(223,'Can change dbversion',65,'change_dbversion'),(224,'Can delete dbversion',65,'delete_dbversion'),(225,'Can add dchecks',66,'add_dchecks'),(226,'Can change dchecks',66,'change_dchecks'),(227,'Can delete dchecks',66,'delete_dchecks'),(228,'Can add dhosts',67,'add_dhosts'),(229,'Can change dhosts',67,'change_dhosts'),(230,'Can delete dhosts',67,'delete_dhosts'),(231,'Can add drules',68,'add_drules'),(232,'Can change drules',68,'change_drules'),(233,'Can delete drules',68,'delete_drules'),(234,'Can add dservices',69,'add_dservices'),(235,'Can change dservices',69,'change_dservices'),(236,'Can delete dservices',69,'delete_dservices'),(237,'Can add escalations',70,'add_escalations'),(238,'Can change escalations',70,'change_escalations'),(239,'Can delete escalations',70,'delete_escalations'),(240,'Can add events',71,'add_events'),(241,'Can change events',71,'change_events'),(242,'Can delete events',71,'delete_events'),(243,'Can add expressions',72,'add_expressions'),(244,'Can change expressions',72,'change_expressions'),(245,'Can delete expressions',72,'delete_expressions'),(246,'Can add functions',73,'add_functions'),(247,'Can change functions',73,'change_functions'),(248,'Can delete functions',73,'delete_functions'),(249,'Can add globalmacro',74,'add_globalmacro'),(250,'Can change globalmacro',74,'change_globalmacro'),(251,'Can delete globalmacro',74,'delete_globalmacro'),(252,'Can add globalvars',75,'add_globalvars'),(253,'Can change globalvars',75,'change_globalvars'),(254,'Can delete globalvars',75,'delete_globalvars'),(255,'Can add graphs items',76,'add_graphsitems'),(256,'Can change graphs items',76,'change_graphsitems'),(257,'Can delete graphs items',76,'delete_graphsitems'),(258,'Can add graph theme',77,'add_graphtheme'),(259,'Can change graph theme',77,'change_graphtheme'),(260,'Can delete graph theme',77,'delete_graphtheme'),(261,'Can add group prototype',78,'add_groupprototype'),(262,'Can change group prototype',78,'change_groupprototype'),(263,'Can delete group prototype',78,'delete_groupprototype'),(264,'Can add history',79,'add_history'),(265,'Can change history',79,'change_history'),(266,'Can delete history',79,'delete_history'),(267,'Can add history log',80,'add_historylog'),(268,'Can change history log',80,'change_historylog'),(269,'Can delete history log',80,'delete_historylog'),(270,'Can add history str',81,'add_historystr'),(271,'Can change history str',81,'change_historystr'),(272,'Can delete history str',81,'delete_historystr'),(273,'Can add history text',82,'add_historytext'),(274,'Can change history text',82,'change_historytext'),(275,'Can delete history text',82,'delete_historytext'),(276,'Can add history uint',83,'add_historyuint'),(277,'Can change history uint',83,'change_historyuint'),(278,'Can delete history uint',83,'delete_historyuint'),(279,'Can add hostmacro',84,'add_hostmacro'),(280,'Can change hostmacro',84,'change_hostmacro'),(281,'Can delete hostmacro',84,'delete_hostmacro'),(282,'Can add hosts groups',85,'add_hostsgroups'),(283,'Can change hosts groups',85,'change_hostsgroups'),(284,'Can delete hosts groups',85,'delete_hostsgroups'),(285,'Can add hosts templates',86,'add_hoststemplates'),(286,'Can change hosts templates',86,'change_hoststemplates'),(287,'Can delete hosts templates',86,'delete_hoststemplates'),(288,'Can add housekeeper',87,'add_housekeeper'),(289,'Can change housekeeper',87,'change_housekeeper'),(290,'Can delete housekeeper',87,'delete_housekeeper'),(291,'Can add httpstep',88,'add_httpstep'),(292,'Can change httpstep',88,'change_httpstep'),(293,'Can delete httpstep',88,'delete_httpstep'),(294,'Can add httpstepitem',89,'add_httpstepitem'),(295,'Can change httpstepitem',89,'change_httpstepitem'),(296,'Can delete httpstepitem',89,'delete_httpstepitem'),(297,'Can add httptest',90,'add_httptest'),(298,'Can change httptest',90,'change_httptest'),(299,'Can delete httptest',90,'delete_httptest'),(300,'Can add httptestitem',91,'add_httptestitem'),(301,'Can change httptestitem',91,'change_httptestitem'),(302,'Can delete httptestitem',91,'delete_httptestitem'),(303,'Can add icon map',92,'add_iconmap'),(304,'Can change icon map',92,'change_iconmap'),(305,'Can delete icon map',92,'delete_iconmap'),(306,'Can add icon mapping',93,'add_iconmapping'),(307,'Can change icon mapping',93,'change_iconmapping'),(308,'Can delete icon mapping',93,'delete_iconmapping'),(309,'Can add ids',94,'add_ids'),(310,'Can change ids',94,'change_ids'),(311,'Can delete ids',94,'delete_ids'),(312,'Can add images',95,'add_images'),(313,'Can change images',95,'change_images'),(314,'Can delete images',95,'delete_images'),(315,'Can add item application prototype',96,'add_itemapplicationprototype'),(316,'Can change item application prototype',96,'change_itemapplicationprototype'),(317,'Can delete item application prototype',96,'delete_itemapplicationprototype'),(318,'Can add item condition',97,'add_itemcondition'),(319,'Can change item condition',97,'change_itemcondition'),(320,'Can delete item condition',97,'delete_itemcondition'),(321,'Can add item discovery',98,'add_itemdiscovery'),(322,'Can change item discovery',98,'change_itemdiscovery'),(323,'Can delete item discovery',98,'delete_itemdiscovery'),(324,'Can add items',99,'add_items'),(325,'Can change items',99,'change_items'),(326,'Can delete items',99,'delete_items'),(327,'Can add items applications',100,'add_itemsapplications'),(328,'Can change items applications',100,'change_itemsapplications'),(329,'Can delete items applications',100,'delete_itemsapplications'),(330,'Can add maintenances',101,'add_maintenances'),(331,'Can change maintenances',101,'change_maintenances'),(332,'Can delete maintenances',101,'delete_maintenances'),(333,'Can add maintenances groups',102,'add_maintenancesgroups'),(334,'Can change maintenances groups',102,'change_maintenancesgroups'),(335,'Can delete maintenances groups',102,'delete_maintenancesgroups'),(336,'Can add maintenances hosts',103,'add_maintenanceshosts'),(337,'Can change maintenances hosts',103,'change_maintenanceshosts'),(338,'Can delete maintenances hosts',103,'delete_maintenanceshosts'),(339,'Can add maintenances windows',104,'add_maintenanceswindows'),(340,'Can change 