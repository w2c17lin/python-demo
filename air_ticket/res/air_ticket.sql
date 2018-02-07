/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : air_ticket

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2018-02-07 14:57:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for air_ticket
-- ----------------------------
DROP TABLE IF EXISTS `air_ticket`;
CREATE TABLE `air_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(255) DEFAULT NULL COMMENT '来源',
  `spider_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `airline` varchar(255) DEFAULT NULL COMMENT '航空公司信息',
  `flight` varchar(255) DEFAULT NULL COMMENT '航班信息',
  `depart_time` varchar(255) DEFAULT NULL COMMENT '出发时间',
  `arrive_time` varchar(255) DEFAULT NULL COMMENT '到达时间',
  `space_time` varchar(255) DEFAULT NULL COMMENT '花费时间',
  `depart_airport` varchar(255) DEFAULT NULL COMMENT '出发机场',
  `arrive_airport` varchar(255) DEFAULT NULL COMMENT '到达机场',
  `price` decimal(10,2) DEFAULT NULL COMMENT '价格',
  `create_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of air_ticket
-- ----------------------------
INSERT INTO `air_ticket` VALUES ('5', '去哪儿', '2018-02-07 14:56:02', '海南航空', 'HU7162 波音787(大)', '20:15', '22:50', '2小时35分钟', '江北机场T3', '首都机场T1', '680.00', '2018-02-07 14:56:02', null);
INSERT INTO `air_ticket` VALUES ('6', '去哪儿', '2018-02-07 14:56:04', '华夏航空', 'G55002 空客321(中)', '19:30', '22:10', '2小时40分钟', '江北机场T3', '首都机场T2', '580.00', '2018-02-07 14:56:04', null);
INSERT INTO `air_ticket` VALUES ('7', '去哪儿', '2018-02-07 14:56:05', '中国国航', 'CA1412 空客330(宽)', '19:15', '22:05', '2小时50分钟', '江北机场T3', '首都机场T3', '620.00', '2018-02-07 14:56:06', null);
INSERT INTO `air_ticket` VALUES ('8', '去哪儿', '2018-02-07 14:56:07', '华夏航空', 'G54056 空客330(宽)', '19:15', '22:05', '2小时50分钟', '江北机场T3', '首都机场T3', '608.00', '2018-02-07 14:56:07', null);
INSERT INTO `air_ticket` VALUES ('9', '去哪儿', '2018-02-07 14:56:08', '四川航空', '3U8515 空客319(中)', '18:35', '21:15', '2小时40分钟', '江北机场T2A', '首都机场T3', '630.00', '2018-02-07 14:56:09', null);
INSERT INTO `air_ticket` VALUES ('10', '去哪儿', '2018-02-07 14:56:10', '南方航空', 'CZ9899 空客321(中)', '13:05', '15:45', '2小时40分钟', '江北机场T2A', '首都机场T3', '890.00', '2018-02-07 14:56:10', null);
INSERT INTO `air_ticket` VALUES ('11', '去哪儿', '2018-02-07 14:56:11', '山东航空', 'SC3073 空客321(中)', '13:05', '15:45', '2小时40分钟', '江北机场T2A', '首都机场T3', '781.00', '2018-02-07 14:56:12', null);
INSERT INTO `air_ticket` VALUES ('12', '去哪儿', '2018-02-07 14:56:13', '南方航空', 'CZ3260 空客321(中)', '11:25', '14:05', '2小时40分钟', '江北机场T3', '首都机场T2', '720.00', '2018-02-07 14:56:13', null);
INSERT INTO `air_ticket` VALUES ('13', '去哪儿', '2018-02-07 14:56:14', '南方航空', 'CZ8101 空客320(中)', '08:00', '10:35', '2小时35分钟', '江北机场T3', '首都机场T2', '640.00', '2018-02-07 14:56:14', null);
INSERT INTO `air_ticket` VALUES ('14', '去哪儿', '2018-02-07 14:56:16', '西藏航空', 'TV6751 波音738(中)', '07:00', '09:40', '2小时40分钟', '江北机场T3', '首都机场T3', '859.00', '2018-02-07 14:56:16', null);
