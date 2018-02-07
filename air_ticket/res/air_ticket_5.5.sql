/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50537
Source Host           : localhost:3306
Source Database       : air_ticket

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2018-02-07 20:13:44
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for air_ticket
-- ----------------------------
DROP TABLE IF EXISTS `air_ticket`;
CREATE TABLE `air_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(255) DEFAULT NULL COMMENT '来源',
  `spider_time` datetime DEFAULT NULL COMMENT '爬取时间',
  `airline` varchar(255) DEFAULT NULL COMMENT '航空公司信息',
  `flight` varchar(255) DEFAULT NULL COMMENT '航班信息',
  `depart_time` varchar(255) DEFAULT NULL COMMENT '出发时间',
  `arrive_time` varchar(255) DEFAULT NULL COMMENT '到达时间',
  `space_time` varchar(255) DEFAULT NULL COMMENT '花费时间',
  `depart_airport` varchar(255) DEFAULT NULL COMMENT '出发机场',
  `arrive_airport` varchar(255) DEFAULT NULL COMMENT '到达机场',
  `price` decimal(10,2) DEFAULT NULL COMMENT '价格',
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of air_ticket
-- ----------------------------
