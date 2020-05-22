/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50640
 Source Host           : localhost:3306
 Source Schema         : python_spider

 Target Server Type    : MySQL
 Target Server Version : 50640
 File Encoding         : 65001

 Date: 23/05/2020 00:38:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for douban
-- ----------------------------
DROP TABLE IF EXISTS `douban`;
CREATE TABLE `douban` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `movie_id` int(25) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `rate` varchar(20) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1961 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
