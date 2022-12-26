/*
Navicat MySQL Data Transfer

Source Server         : mybatis
Source Server Version : 50635
Source Host           : localhost:3306
Source Database       : hrms

Target Server Type    : MYSQL
Target Server Version : 50635
File Encoding         : 65001

Date: 2022-12-26 18:36:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_admin
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_admin
-- ----------------------------
INSERT INTO `t_admin` VALUES ('1', 'lx', 'lx');
INSERT INTO `t_admin` VALUES ('2', 'll', 'll');

-- ----------------------------
-- Table structure for t_application
-- ----------------------------
DROP TABLE IF EXISTS `t_application`;
CREATE TABLE `t_application` (
  `applic_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `sex` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `birth` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `time` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`applic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_application
-- ----------------------------
INSERT INTO `t_application` VALUES ('1', '钟灏', '男', '2002-04-27', '15910018009', '3162146207@qq.com', '2015-08-03');
INSERT INTO `t_application` VALUES ('2', '李伯', '男', '2000-07-22', '17728263793', '3182556825@qq.com', '2011-04-23');
INSERT INTO `t_application` VALUES ('3', '邱达', '男', '2001-07-07', '18175309447', '8683812105@qq.com', '2010-06-12');
INSERT INTO `t_application` VALUES ('4', '谭梁', '男', '2000-09-13', '18816435123', '0103204340@qq.com', '2015-10-28');
INSERT INTO `t_application` VALUES ('5', '尹擎', '男', '2001-03-31', '18699274726', '4076670105@qq.com', '2015-12-14');
INSERT INTO `t_application` VALUES ('6', '陆晋', '男', '2002-10-16', '17368343879', '7135352230@qq.com', '2014-01-27');
INSERT INTO `t_application` VALUES ('7', '何溢', '男', '2001-04-20', '18801473767', '1424710485@qq.com', '2014-04-03');
INSERT INTO `t_application` VALUES ('8', '史安', '男', '2000-01-31', '18305957898', '1231188250@qq.com', '2011-01-06');
INSERT INTO `t_application` VALUES ('10', '乔圣', '男', '2001-11-18', '13335236204', '7104706384@qq.com', '2012-07-29');
INSERT INTO `t_application` VALUES ('11', '易炜', '男', '2000-12-13', '13662114928', '7424447144@qq.com', '2014-04-13');
INSERT INTO `t_application` VALUES ('12', '夏启', '男', '2000-12-14', '18808162362', '6862813758@qq.com', '2015-07-30');
INSERT INTO `t_application` VALUES ('13', '蔡乾', '男', '2002-01-28', '13501401996', '3552781730@qq.com', '2010-04-17');
INSERT INTO `t_application` VALUES ('14', '漕骄', '男', '2002-07-08', '13400117245', '1431256683@qq.com', '2011-04-11');
INSERT INTO `t_application` VALUES ('15', '龙虚', '男', '2002-12-26', '14557115912', '0584874656@qq.com', '2011-01-02');
INSERT INTO `t_application` VALUES ('16', '宋选', '男', '2000-08-24', '15519048158', '6878028054@qq.com', '2013-01-08');
INSERT INTO `t_application` VALUES ('17', '贾弓', '男', '2002-07-23', '13835602953', '2873225502@qq.com', '2010-06-15');
INSERT INTO `t_application` VALUES ('18', '石部', '男', '2001-01-03', '15123108878', '3571875028@qq.com;', '2010-07-29');
INSERT INTO `t_application` VALUES ('19', '阎绮', '男', '2003-05-20', '13318716680', '3571875029@qq.com', '2013-04-27');
INSERT INTO `t_application` VALUES ('20', '白宪', '男', '2001-05-21', '13001565229', '3571875030@qq.com', '2015-06-22');
INSERT INTO `t_application` VALUES ('21', '冯益', '男', '2001-05-05', '14990764657', '5461542154@qq.com', '2013-01-10');
INSERT INTO `t_application` VALUES ('22', '段启', '男', '2001-05-08', '13239788689', '2862200502@qq.com', '2014-05-06');
INSERT INTO `t_application` VALUES ('23', '沈旁', '男', '2000-11-16', '19950827203', '5776076200@qq.com', '2010-08-01');
INSERT INTO `t_application` VALUES ('24', '叶问', '男', '2000-12-01', '15549489745', '5140555416@qq.com', '2012-11-25');
INSERT INTO `t_application` VALUES ('25', '范建', '男', '2003-09-12', '17126137931', '1174646823@qq.com', '2014-05-25');
INSERT INTO `t_application` VALUES ('26', '宋辈', '男', '2000-06-25', '18012388599', '1837378232@qq.com', '2011-05-27');
INSERT INTO `t_application` VALUES ('27', '马势', '男', '2003-12-30', '13236599182', '3440003665@qq.com', '2011-04-04');
INSERT INTO `t_application` VALUES ('28', '黎福', '男', '2001-02-01', '15064324236', '3542040204@qq.com', '2010-03-30');
INSERT INTO `t_application` VALUES ('29', '周启', '男', '2002-09-09', '13795968051', '1785866657@qq.com', '2010-10-14');
INSERT INTO `t_application` VALUES ('30', '钱畴', '男', '2003-09-20', '15654255690', '6217365645@qq.com', '2010-05-06');
INSERT INTO `t_application` VALUES ('31', '任俣', '男', '2002-08-24', '15563335316', '1815843168@qq.com', '2011-05-07');
INSERT INTO `t_application` VALUES ('32', '萧木', '男', '2003-11-23', '13224832307', '7527154713@qq.com', '2014-08-06');
INSERT INTO `t_application` VALUES ('33', '金舷', '男', '2002-12-09', '17833246719', '3608804683@qq.com', '2012-12-21');
INSERT INTO `t_application` VALUES ('34', '宋钧', '男', '2001-04-17', '14742156641', '7274315263@qq.com', '2011-08-02');
INSERT INTO `t_application` VALUES ('35', '何俊', '男', '2000-02-17', '18318176960', '2586810366@qq.com', '2012-07-31');
INSERT INTO `t_application` VALUES ('36', '夏延', '男', '2001-08-14', '16528186543', '1750137267@qq.com', '2010-03-29');
INSERT INTO `t_application` VALUES ('37', '金尧', '男', '2001-09-17', '15311023843', '0623057638@qq.com', '2013-10-21');
INSERT INTO `t_application` VALUES ('38', '谢以', '男', '2003-10-18', '15314217383', '8216176387@qq.com', '2010-11-15');
INSERT INTO `t_application` VALUES ('39', '黎莱', '男', '2001-01-25', '18446997013', '0081105620@qq.com', '2014-06-18');
INSERT INTO `t_application` VALUES ('40', '贺昌', '男', '2003-08-01', '18366216784', '2347242563@qq.com', '2015-07-14');
INSERT INTO `t_application` VALUES ('41', '杨丞', '男', '2001-07-16', '14565443603', '2286785783@qq.com', '2015-01-17');
INSERT INTO `t_application` VALUES ('42', '汤璥', '男', '2003-02-15', '17867236068', '5134154135@qq.com', '2011-07-19');
INSERT INTO `t_application` VALUES ('43', '易劼', '男', '2000-02-15', '13136827290', '6428707028@qq.com', '2013-11-22');
INSERT INTO `t_application` VALUES ('44', '马珹', '男', '2002-05-19', '15224215384', '8043657336@qq.com', '2010-09-14');
INSERT INTO `t_application` VALUES ('45', '林馗', '男', '2002-07-18', '15015227559', '4054460232@qq.com', '2014-01-26');
INSERT INTO `t_application` VALUES ('46', '魏功', '男', '2002-02-14', '13244029613', '4677260482@qq.com', '2012-09-10');
INSERT INTO `t_application` VALUES ('47', '钱蔚', '男', '2003-12-25', '18021705760', '6236417502@qq.com', '2011-07-11');
INSERT INTO `t_application` VALUES ('48', '漕剑', '男', '2003-10-17', '13039523899', '1141857641@qq.com', '2010-01-12');
INSERT INTO `t_application` VALUES ('49', '梁律', '男', '2002-09-20', '13829963695', '8560412508@qq.com', '2012-11-25');
INSERT INTO `t_application` VALUES ('50', '薛元', '男', '2000-05-15', '17521185244', '4240026802@qq.com', '2014-01-03');
INSERT INTO `t_application` VALUES ('51', '叶余馥', '女', '2001-12-24', '17639687142', '8411122585@qq.com', '2015-12-08');
INSERT INTO `t_application` VALUES ('52', '刘含蕾', '女', '2000-12-10', '15528437370', '8206314323@qq.com', '2011-01-03');
INSERT INTO `t_application` VALUES ('53', '范晏如', '女', '2003-08-12', '15174867488', '8151676415@qq.com', '2013-03-16');
INSERT INTO `t_application` VALUES ('54', '赖安蕾', '女', '2001-05-11', '13374092953', '7861233571@qq.com', '2015-08-25');
INSERT INTO `t_application` VALUES ('55', '谭龙艳', '女', '2003-09-14', '14791756287', '7563012658@qq.com', '2010-04-13');
INSERT INTO `t_application` VALUES ('56', '朱野雪', '女', '2003-11-22', '13882169306', '6355368032@qq.com', '2012-09-23');
INSERT INTO `t_application` VALUES ('57', '江晨钰', '女', '2001-07-17', '15320025648', '4732785740@qq.com', '2011-10-15');
INSERT INTO `t_application` VALUES ('58', '贺雪冰', '女', '2003-12-28', '15537238675', '6840424115@qq.com', '2012-10-12');
INSERT INTO `t_application` VALUES ('59', '唐珑玲', '女', '2001-08-17', '13463357644', '4072833074@qq.com', '2015-09-30');
INSERT INTO `t_application` VALUES ('60', '彭西华', '女', '2002-12-20', '15238041575', '4325601350@qq.com', '2010-05-01');
INSERT INTO `t_application` VALUES ('61', '郝语风', '女', '2000-11-02', '18362177843', '4415178400@qq.com', '2014-07-24');
INSERT INTO `t_application` VALUES ('62', '谢婧玟', '女', '2002-10-22', '15312375950', '2686638133@qq.com', '2010-09-05');
INSERT INTO `t_application` VALUES ('63', '廖珉瑶', '女', '2001-12-26', '15288598767', '5131353153@qq.com', '2010-10-25');
INSERT INTO `t_application` VALUES ('64', '邓琼怡', '女', '2001-05-27', '18673076852', '5480435734@qq.com', '2015-04-09');
INSERT INTO `t_application` VALUES ('65', '朱冰蝶', '女', '2002-04-19', '15605228988', '1040007210@qq.com', '2010-10-19');
INSERT INTO `t_application` VALUES ('66', '宋楠楠', '女', '2002-08-01', '13593116148', '4787164472@qq.com', '2013-04-18');
INSERT INTO `t_application` VALUES ('67', '唐思楠', '女', '2003-01-03', '15601631789', '0082405107@qq.com', '2010-05-26');
INSERT INTO `t_application` VALUES ('68', '郭知世', '女', '2002-03-18', '15522305529', '1015712766@qq.com', '2012-05-05');
INSERT INTO `t_application` VALUES ('69', '叶冰萍', '女', '2000-08-27', '13108586104', '4603774077@qq.com', '2011-01-19');
INSERT INTO `t_application` VALUES ('70', '石孟乐', '女', '2000-07-23', '18536619476', '7100401250@qq.com', '2015-02-01');
INSERT INTO `t_application` VALUES ('71', '傅莉颖', '女', '2001-10-24', '13225018933', '4612735388@qq.com', '2011-12-05');
INSERT INTO `t_application` VALUES ('72', '罗歌玲', '女', '2002-09-04', '17811345820', '4560620536@qq.com', '2014-01-10');
INSERT INTO `t_application` VALUES ('73', '于雅香', '女', '2001-01-28', '13554809177', '4422800106@qq.com', '2013-09-29');
INSERT INTO `t_application` VALUES ('74', '叶从波', '女', '2003-03-09', '13470477046', '0825275654@qq.com', '2011-02-20');
INSERT INTO `t_application` VALUES ('75', '文秋芳', '女', '2001-04-11', '18815195864', '1117323821@qq.com', '2012-12-04');
INSERT INTO `t_application` VALUES ('76', '蔡凝珍', '女', '2002-01-13', '19917583233', '0578583837@qq.com', '2012-06-01');
INSERT INTO `t_application` VALUES ('77', '卢元英', '女', '2001-04-02', '17236506880', '2421843078@qq.com', '2011-05-21');
INSERT INTO `t_application` VALUES ('78', '夏小溪', '女', '2003-01-16', '19973467037', '6287433386@qq.com', '2013-06-21');
INSERT INTO `t_application` VALUES ('79', '唐湛恩', '女', '2003-10-02', '15235877496', '5178640302@qq.com', '2010-04-25');
INSERT INTO `t_application` VALUES ('80', '任春华', '女', '2001-02-28', '15545803809', '3637267887@qq.com', '2013-10-09');
INSERT INTO `t_application` VALUES ('81', '邹新林', '女', '2003-03-31', '18735764472', '8303475042@qq.com', '2011-01-04');
INSERT INTO `t_application` VALUES ('82', '高步美', '女', '2003-12-06', '19842653529', '5806115343@qq.com', '2013-01-12');
INSERT INTO `t_application` VALUES ('83', '文寻云', '女', '2002-04-28', '13197126828', '3805407156@qq.com', '2015-06-20');
INSERT INTO `t_application` VALUES ('84', '姚紫翠', '女', '2002-08-23', '15146842370', '4213521231@qq.com', '2011-08-08');
INSERT INTO `t_application` VALUES ('85', '谭子美', '女', '2003-06-09', '15773916086', '4340620437@qq.com', '2014-04-21');
INSERT INTO `t_application` VALUES ('86', '陈秀越', '女', '2003-02-06', '13862614043', '7087535650@qq.com', '2012-06-15');
INSERT INTO `t_application` VALUES ('87', '秦赞悦', '女', '2001-12-07', '18207001913', '1434483474@qq.com', '2011-01-17');
INSERT INTO `t_application` VALUES ('88', '武巧春', '女', '2002-11-28', '15069929678', '8336624888@qq.com', '2013-10-29');
INSERT INTO `t_application` VALUES ('89', '乔永茹', '女', '2000-06-12', '16531956874', '0185420181@qq.com', '2015-09-01');
INSERT INTO `t_application` VALUES ('90', '余怀萍', '女', '2001-02-28', '13436045611', '3154508857@qq.com', '2010-12-26');
INSERT INTO `t_application` VALUES ('91', '于醉卉', '女', '2000-03-26', '13394725936', '8468845113@qq.com', '2014-06-21');
INSERT INTO `t_application` VALUES ('92', '史依丝', '女', '2002-11-22', '15620658514', '7675804781@qq.com', '2012-02-01');
INSERT INTO `t_application` VALUES ('93', '江小枫', '女', '2000-02-26', '16516821662', '7155066816@qq.com', '2015-11-21');
INSERT INTO `t_application` VALUES ('94', '赖慧君', '女', '2002-01-04', '15832442718', '2531054060@qq.com', '2014-12-11');
INSERT INTO `t_application` VALUES ('95', '贺怡若', '女', '2002-12-24', '15276434282', '6804253045@qq.com', '2015-03-15');
INSERT INTO `t_application` VALUES ('96', '贾怡宁', '女', '2003-06-16', '15594936823', '5183868071@qq.com', '2010-11-30');
INSERT INTO `t_application` VALUES ('97', '王静曼', '女', '2000-07-01', '13434393090', '6684122653@qq.com', '2012-03-04');
INSERT INTO `t_application` VALUES ('98', '梁艳霞', '女', '2000-09-20', '13489539500', '5418471134@qq.com', '2012-02-13');

-- ----------------------------
-- Table structure for t_check
-- ----------------------------
DROP TABLE IF EXISTS `t_check`;
CREATE TABLE `t_check` (
  `check_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `type` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `money` int(11) NOT NULL,
  `check_peo` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`check_id`),
  KEY `FK_staff_check` (`staff_id`),
  CONSTRAINT `FK_staff_check` FOREIGN KEY (`staff_id`) REFERENCES `t_staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_check
-- ----------------------------
INSERT INTO `t_check` VALUES ('56', '56', '出差', '1000000', 'aaa');
INSERT INTO `t_check` VALUES ('57', '57', '加班', '200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('58', '58', '调班', '-200', '刘杰');
INSERT INTO `t_check` VALUES ('59', '59', '旷工', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('60', '60', '加班', '200', '刘熙');
INSERT INTO `t_check` VALUES ('61', '61', '出差', '200', '刘杰');
INSERT INTO `t_check` VALUES ('62', '62', '迟到', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('63', '63', '调班', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('64', '64', '出差', '200', '马椿淋');
INSERT INTO `t_check` VALUES ('65', '65', '旷工', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('66', '66', '迟到', '-200', '刘熙');
INSERT INTO `t_check` VALUES ('67', '67', '迟到', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('68', '68', '调班', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('69', '69', '调班', '-200', '刘熙');
INSERT INTO `t_check` VALUES ('70', '70', '请假', '-200', '刘杰');
INSERT INTO `t_check` VALUES ('71', '71', '旷工', '-200', '刘杰');
INSERT INTO `t_check` VALUES ('72', '72', '旷工', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('73', '73', '旷工', '-200', '刘熙');
INSERT INTO `t_check` VALUES ('74', '74', '调班', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('75', '75', '请假', '-200', '刘杰');
INSERT INTO `t_check` VALUES ('76', '76', '请假', '-200', '刘熙');
INSERT INTO `t_check` VALUES ('77', '77', '旷工', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('78', '78', '旷工', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('79', '79', '迟到', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('80', '80', '出差', '200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('81', '81', '调班', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('82', '82', '出差', '200', '刘熙');
INSERT INTO `t_check` VALUES ('83', '83', '出差', '200', '刘杰');
INSERT INTO `t_check` VALUES ('84', '84', '加班', '200', '马椿淋');
INSERT INTO `t_check` VALUES ('85', '85', '加班', '200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('86', '86', '请假', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('87', '87', '加班', '200', '刘杰');
INSERT INTO `t_check` VALUES ('88', '88', '旷工', '-200', '刘熙');
INSERT INTO `t_check` VALUES ('89', '89', '旷工', '-200', '刘杰');
INSERT INTO `t_check` VALUES ('90', '90', '旷工', '-200', '刘杰');
INSERT INTO `t_check` VALUES ('91', '91', '出差', '200', '刘杰');
INSERT INTO `t_check` VALUES ('92', '92', '旷工', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('93', '93', '调班', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('94', '94', '旷工', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('95', '95', '调班', '-200', '马椿淋');
INSERT INTO `t_check` VALUES ('96', '96', '出差', '200', '马椿淋');
INSERT INTO `t_check` VALUES ('97', '97', '迟到', '-200', '刘熙');
INSERT INTO `t_check` VALUES ('98', '98', '调班', '-200', '皱鑫阳');
INSERT INTO `t_check` VALUES ('99', '99', '出差', '200', '刘熙');
INSERT INTO `t_check` VALUES ('100', '100', '请假', '-200', '刘熙');

-- ----------------------------
-- Table structure for t_contract
-- ----------------------------
DROP TABLE IF EXISTS `t_contract`;
CREATE TABLE `t_contract` (
  `contract_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `start_day` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `end_day` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `duty` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `content` text COLLATE utf8_unicode_ci NOT NULL,
  `remark` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`contract_id`),
  KEY `FK_staff_contract` (`staff_id`),
  CONSTRAINT `FK_staff_contract` FOREIGN KEY (`staff_id`) REFERENCES `t_staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_contract
-- ----------------------------
INSERT INTO `t_contract` VALUES ('57', '57', '2011-10-15', '2030-06-19', '部长', '《中华人民共和国民法典》第一百条到一百五十条,111111', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('58', '58', '2012-10-12', '2029-06-18', '部长', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('59', '59', '2015-09-30', '2029-09-20', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('60', '60', '2010-05-01', '2030-07-22', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('61', '61', '2014-07-24', '2030-11-30', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('62', '62', '2010-09-05', '2029-12-21', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('63', '63', '2010-10-25', '2030-05-19', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('64', '64', '2015-04-09', '2029-12-01', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('65', '65', '2010-10-19', '2029-01-08', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('66', '66', '2013-04-18', '2029-07-29', '经理', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('67', '67', '2010-05-26', '2030-10-10', '经理', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('68', '68', '2012-05-05', '2029-01-10', '经理', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('69', '69', '2011-01-19', '2030-08-29', '经理', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('70', '70', '2015-02-01', '2029-10-31', '部长', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('71', '71', '2011-12-05', '2030-09-07', '部长', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('72', '72', '2014-01-10', '2029-09-05', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('73', '73', '2013-09-29', '2029-08-06', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('74', '74', '2011-02-20', '2030-07-23', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('75', '75', '2012-12-04', '2030-11-01', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('76', '76', '2012-06-01', '2029-03-26', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('77', '77', '2011-05-21', '2030-11-17', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('78', '78', '2013-06-21', '2030-02-09', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('79', '79', '2010-04-25', '2030-07-03', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('80', '80', '2013-10-09', '2030-07-02', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('81', '81', '2011-01-04', '2029-12-15', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('82', '82', '2013-01-12', '2030-08-13', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('83', '83', '2015-06-20', '2029-04-03', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('84', '84', '2011-08-08', '2029-08-28', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('85', '85', '2014-04-21', '2029-12-30', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('86', '86', '2012-06-15', '2029-08-28', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('87', '87', '2011-01-17', '2030-03-28', '经理', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('88', '88', '2013-10-29', '2030-09-07', '经理', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('89', '89', '2015-09-01', '2030-10-27', '部长', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('90', '90', '2010-12-26', '2029-05-13', '部长', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('91', '91', '2014-06-21', '2029-11-25', '部长', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('92', '92', '2012-02-01', '2030-12-19', '部长', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('93', '93', '2015-11-21', '2030-02-26', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('94', '94', '2014-12-11', '2030-09-22', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('95', '95', '2015-03-15', '2030-06-13', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('96', '96', '2010-11-30', '2030-12-21', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('97', '97', '2012-03-04', '2030-06-13', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('98', '98', '2012-02-13', '2030-04-01', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('99', '99', '2014-09-08', '2029-03-25', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('100', '100', '2011-11-07', '2029-04-13', '员工', '《中华人民共和国民法典》第一百条到一百五十条', '违约赔偿双倍工资');
INSERT INTO `t_contract` VALUES ('101', '56', '2022-12-06', '2022-12-22', '111', '111', '111');

-- ----------------------------
-- Table structure for t_pay
-- ----------------------------
DROP TABLE IF EXISTS `t_pay`;
CREATE TABLE `t_pay` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `base_pay` int(11) NOT NULL,
  `merit_pay` int(11) NOT NULL,
  `bonus` int(11) DEFAULT NULL,
  `fine` int(11) DEFAULT NULL,
  `total` int(11) NOT NULL,
  `get_time` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`pay_id`),
  KEY `FK_staff_pay` (`staff_id`),
  CONSTRAINT `FK_staff_pay` FOREIGN KEY (`staff_id`) REFERENCES `t_staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_pay
-- ----------------------------
INSERT INTO `t_pay` VALUES ('56', '56', '40000', '2055', '1000000', '-200000', '842055', '2020-12-24');
INSERT INTO `t_pay` VALUES ('57', '57', '35000', '2056', '200', '200', '37456', '2021-12-18');
INSERT INTO `t_pay` VALUES ('58', '58', '35000', '2057', '500', '-200', '37357', '2021-03-10');
INSERT INTO `t_pay` VALUES ('59', '59', '35000', '2058', '500', '-200', '37358', '2021-02-15');
INSERT INTO `t_pay` VALUES ('60', '60', '35000', '2059', '200', '200', '37459', '2021-09-18');
INSERT INTO `t_pay` VALUES ('61', '61', '35000', '-2000', '200', '200', '33400', '2020-11-20');
INSERT INTO `t_pay` VALUES ('62', '62', '35000', '-2001', '500', '-200', '33299', '2020-12-17');
INSERT INTO `t_pay` VALUES ('63', '63', '35000', '-2002', '500', '-200', '33298', '2022-04-02');
INSERT INTO `t_pay` VALUES ('64', '64', '35000', '-2003', '200', '200', '33397', '2021-07-15');
INSERT INTO `t_pay` VALUES ('65', '65', '35000', '-2004', '500', '-200', '33296', '2020-10-25');
INSERT INTO `t_pay` VALUES ('66', '66', '35000', '-2005', '500', '-200', '33295', '2021-11-03');
INSERT INTO `t_pay` VALUES ('67', '67', '35000', '-2006', '500', '-200', '33294', '2020-01-14');
INSERT INTO `t_pay` VALUES ('68', '68', '35000', '-2007', '500', '-200', '33293', '2020-03-27');
INSERT INTO `t_pay` VALUES ('69', '69', '35000', '-2008', '500', '-200', '33292', '2021-07-06');
INSERT INTO `t_pay` VALUES ('70', '70', '35000', '-2009', '500', '-200', '33291', '2021-01-06');
INSERT INTO `t_pay` VALUES ('71', '71', '35000', '-2010', '500', '-200', '33290', '2021-02-08');
INSERT INTO `t_pay` VALUES ('72', '72', '35000', '-2011', '500', '-200', '33289', '2021-06-25');
INSERT INTO `t_pay` VALUES ('73', '73', '35000', '-2012', '500', '-200', '33288', '2021-02-27');
INSERT INTO `t_pay` VALUES ('74', '74', '35000', '-2013', '500', '-200', '33287', '2020-05-09');
INSERT INTO `t_pay` VALUES ('75', '75', '35000', '-2014', '1000', '-200', '33786', '2020-12-24');
INSERT INTO `t_pay` VALUES ('76', '76', '35000', '-2015', '1000', '-200', '33785', '2020-06-27');
INSERT INTO `t_pay` VALUES ('77', '77', '35000', '-2016', '1000', '-200', '33784', '2022-01-18');
INSERT INTO `t_pay` VALUES ('78', '78', '35000', '-2017', '1000', '-200', '33783', '2021-07-18');
INSERT INTO `t_pay` VALUES ('79', '79', '35000', '-2018', '1000', '-200', '33782', '2021-04-23');
INSERT INTO `t_pay` VALUES ('80', '80', '35000', '-2019', '200', '200', '33381', '2021-04-13');
INSERT INTO `t_pay` VALUES ('81', '81', '35000', '-2020', '1000', '-200', '33780', '2020-09-12');
INSERT INTO `t_pay` VALUES ('82', '82', '35000', '-2021', '200', '200', '33379', '2022-01-21');
INSERT INTO `t_pay` VALUES ('83', '83', '35000', '-2022', '200', '200', '33378', '2021-04-08');
INSERT INTO `t_pay` VALUES ('84', '84', '35000', '-2023', '200', '100', '33277', '2021-11-28');
INSERT INTO `t_pay` VALUES ('85', '85', '35000', '-2024', '200', '100', '33276', '2020-07-19');
INSERT INTO `t_pay` VALUES ('86', '86', '200', '200', '0', '-200', '200', '2022-12-11');
INSERT INTO `t_pay` VALUES ('87', '87', '35000', '-2026', '200', '100', '33274', '2021-11-19');
INSERT INTO `t_pay` VALUES ('88', '88', '35000', '-2027', '1000', '-200', '33773', '2022-04-15');
INSERT INTO `t_pay` VALUES ('89', '89', '35000', '-2028', '1000', '-200', '33772', '2021-07-19');
INSERT INTO `t_pay` VALUES ('90', '90', '35000', '-2029', '1000', '-200', '33771', '2021-05-08');
INSERT INTO `t_pay` VALUES ('91', '91', '35000', '-2030', '200', '100', '33270', '2020-04-14');
INSERT INTO `t_pay` VALUES ('92', '92', '35000', '-2031', '1000', '-200', '33769', '2021-08-07');
INSERT INTO `t_pay` VALUES ('93', '93', '35000', '-2032', '1000', '-200', '33768', '2021-02-23');
INSERT INTO `t_pay` VALUES ('94', '94', '35000', '-2033', '1000', '-200', '33767', '2020-12-10');
INSERT INTO `t_pay` VALUES ('95', '95', '35000', '-2034', '1000', '-200', '33766', '2020-06-26');
INSERT INTO `t_pay` VALUES ('96', '96', '35000', '-2035', '200', '100', '33265', '2020-03-25');
INSERT INTO `t_pay` VALUES ('97', '97', '35000', '-2036', '1000', '-200', '33764', '2021-09-10');
INSERT INTO `t_pay` VALUES ('98', '98', '35000', '-2037', '1000', '-200', '33763', '2021-12-22');
INSERT INTO `t_pay` VALUES ('99', '99', '35000', '-2038', '200', '100', '33262', '2020-04-09');
INSERT INTO `t_pay` VALUES ('100', '100', '35000', '-2039', '1000', '-200', '33761', '2021-11-29');

-- ----------------------------
-- Table structure for t_personal_trans
-- ----------------------------
DROP TABLE IF EXISTS `t_personal_trans`;
CREATE TABLE `t_personal_trans` (
  `pertra_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `last_section` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `next_section` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `last_duty` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `next_duty` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `trans_time` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `causee` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`pertra_id`),
  KEY `FK_staff_per` (`staff_id`),
  CONSTRAINT `FK_staff_per` FOREIGN KEY (`staff_id`) REFERENCES `t_staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_personal_trans
-- ----------------------------
INSERT INTO `t_personal_trans` VALUES ('68', '68', '人力资源部', '行政部', '部长', '经理', '2020-12-26', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('69', '69', '人力资源部', '行政部', '部长', '经理', '2021-08-04', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('70', '70', '人力资源部', '行政部', '员工', '部长', '2020-02-08', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('71', '71', '人力资源部', '行政部', '员工', '部长', '2021-01-18', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('72', '72', '人力资源部', '行政部', '经理', '员工', '2022-05-27', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('73', '73', '人力资源部', '行政部', '经理', '员工', '2021-03-26', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('74', '74', '人力资源部', '行政部', '经理', '员工', '2020-07-01', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('75', '75', '人力资源部', '行政部', '经理', '员工', '2020-08-21', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('83', '83', '人力资源部', '后勤部', '经理', '员工', '2020-01-01', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('84', '84', '人力资源部', '行政部', '经理', '员工', '2022-01-27', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('85', '85', '人力资源部', '行政部', '经理', '员工', '2021-02-22', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('86', '86', '人力资源部', '行政部', '经理', '员工', '2022-02-06', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('87', '87', '后勤部', '人力资源部', '部长', '经理', '2022-09-07', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('88', '88', '后勤部', '人力资源部', '部长', '经理', '2022-12-15', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('89', '89', '后勤部', '人力资源部', '员工', '部长', '2020-10-01', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('90', '90', '后勤部', '人力资源部', '员工', '部长', '2022-05-11', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('91', '91', '后勤部', '人力资源部', '员工', '部长', '2021-11-28', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('92', '92', '后勤部', '人力资源部', '员工', '部长', '2022-03-19', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('93', '93', '后勤部', '人力资源部', '部长', '员工', '2021-08-03', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('94', '94', '后勤部', '人力资源部', '部长', '员工', '2021-04-11', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('95', '95', '后勤部', '人力资源部', '部长', '员工', '2020-12-11', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('96', '96', '后勤部', '人力资源部', '部长', '员工', '2021-11-12', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('98', '98', '后勤部', '人力资源部', '部长', '员工', '2021-07-23', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('99', '99', '后勤部', '人力资源部', '部长', '员工', '2022-05-25', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('100', '100', '后勤部', '人力资源部', '部长', '员工', '2021-01-24', '有利于公司的效率和效益的提高');
INSERT INTO `t_personal_trans` VALUES ('101', '56', '生产部', '后勤部', 'cscac', 'cacac', '2022-12-07', '无');

-- ----------------------------
-- Table structure for t_record
-- ----------------------------
DROP TABLE IF EXISTS `t_record`;
CREATE TABLE `t_record` (
  `record_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `record_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `digest` text COLLATE utf8_unicode_ci NOT NULL,
  `remark` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`record_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_record
-- ----------------------------
INSERT INTO `t_record` VALUES ('57', '57', '江晨钰', '具备较强的逻辑思维方式，对事情认真负责，能吃苦受累，有很强的责任心和团队意识;自信、乐观，具有一定的创新意识。', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('58', '58', '贺雪冰', '具备较强的逻辑思维方式，对事情认真负责，能吃苦受累，有很强的责任心和团队意识;自信、乐观，具有一定的创新意识。', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('59', '59', '唐珑玲', '具备较强的逻辑思维方式，对事情认真负责，能吃苦受累，有很强的责任心和团队意识;自信、乐观，具有一定的创新意识。', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('60', '60', '彭西华', '具备较强的逻辑思维方式，对事情认真负责，能吃苦受累，有很强的责任心和团队意识;自信、乐观，具有一定的创新意识。', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('61', '61', '郝语风', '具备较强的逻辑思维方式，对事情认真负责，能吃苦受累，有很强的责任心和团队意识;自信、乐观，具有一定的创新意识。', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('62', '62', '谢婧玟', '具备较强的逻辑思维方式，对事情认真负责，能吃苦受累，有很强的责任心和团队意识;自信、乐观，具有一定的创新意识。', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('63', '63', '廖珉瑶', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('64', '64', '邓琼怡', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('65', '65', '朱冰蝶', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '工作雷厉风行，高效快捷');
INSERT INTO `t_record` VALUES ('66', '66', '宋楠楠', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('67', '67', '唐思楠', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('68', '68', '郭知世', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('69', '69', '叶冰萍', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('70', '70', '石孟乐', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('71', '71', '傅莉颖', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('72', '72', '罗歌玲', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('73', '73', '于雅香', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('74', '74', '叶从波', '具有团队精神，能与同事，其它部门积极配合，公司利益至上;', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('75', '75', '文秋芳', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('76', '76', '蔡凝珍', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('77', '77', '卢元英', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('78', '78', '夏小溪', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('79', '79', '唐湛恩', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('80', '80', '任春华', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('81', '81', '邹新林', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('82', '82', '高步美', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('83', '83', '文寻云', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('84', '84', '姚紫翠', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('85', '85', '谭子美', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('86', '86', '陈秀越', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('87', '87', '秦赞悦', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('88', '88', '武巧春', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('89', '89', '乔永茹', '具有亲和力，平易近人。有很强的交流沟通能力，善于表达自我，口才好。观察事物细致入微，能够及时发现和更正自我的不足。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('90', '90', '余怀萍', '热爱学习，工作态度严谨认真，责任心强，有很好的团队合作能力。有良好的分析、解决问题的思维。以创新、解决客户需求、维护公司利益为宗旨。来接受挑战和更大的发展平台。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('91', '91', '于醉卉', '热爱学习，工作态度严谨认真，责任心强，有很好的团队合作能力。有良好的分析、解决问题的思维。以创新、解决客户需求、维护公司利益为宗旨。来接受挑战和更大的发展平台。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('92', '92', '史依丝', '热爱学习，工作态度严谨认真，责任心强，有很好的团队合作能力。有良好的分析、解决问题的思维。以创新、解决客户需求、维护公司利益为宗旨。来接受挑战和更大的发展平台。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('93', '93', '江小枫', '热爱学习，工作态度严谨认真，责任心强，有很好的团队合作能力。有良好的分析、解决问题的思维。以创新、解决客户需求、维护公司利益为宗旨。来接受挑战和更大的发展平台。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('94', '94', '赖慧君', '热爱学习，工作态度严谨认真，责任心强，有很好的团队合作能力。有良好的分析、解决问题的思维。以创新、解决客户需求、维护公司利益为宗旨。来接受挑战和更大的发展平台。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('95', '95', '贺怡若', '热爱学习，工作态度严谨认真，责任心强，有很好的团队合作能力。有良好的分析、解决问题的思维。以创新、解决客户需求、维护公司利益为宗旨。来接受挑战和更大的发展平台。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('96', '96', '贾怡宁', '热爱学习，工作态度严谨认真，责任心强，有很好的团队合作能力。有良好的分析、解决问题的思维。以创新、解决客户需求、维护公司利益为宗旨。来接受挑战和更大的发展平台。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('97', '97', '王静曼', '为人稳重、大方，认真对待工作，开朗自信，待人真诚，有优良的团队精神，强烈的责任心，良好的沟通协调能力。在责任心、事业心、亲和力、决策能力、计划能力、谈判能力强，具备良好的敬业精神和职业道德操守，有很强的\'感召力和凝聚力。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('98', '98', '梁艳霞', '为人稳重、大方，认真对待工作，开朗自信，待人真诚，有优良的团队精神，强烈的责任心，良好的沟通协调能力。在责任心、事业心、亲和力、决策能力、计划能力、谈判能力强，具备良好的敬业精神和职业道德操守，有很强的\'感召力和凝聚力。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('99', '99', '郭和静', '为人稳重、大方，认真对待工作，开朗自信，待人真诚，有优良的团队精神，强烈的责任心，良好的沟通协调能力。在责任心、事业心、亲和力、决策能力、计划能力、谈判能力强，具备良好的敬业精神和职业道德操守，有很强的\'感召力和凝聚力。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');
INSERT INTO `t_record` VALUES ('100', '100', '宋琴心', '为人稳重、大方，认真对待工作，开朗自信，待人真诚，有优良的团队精神，强烈的责任心，良好的沟通协调能力。在责任心、事业心、亲和力、决策能力、计划能力、谈判能力强，具备良好的敬业精神和职业道德操守，有很强的\'感召力和凝聚力。', '待客人如亲人，百拿不厌，百问不厌，受到客人表扬。');

-- ----------------------------
-- Table structure for t_recruit
-- ----------------------------
DROP TABLE IF EXISTS `t_recruit`;
CREATE TABLE `t_recruit` (
  `recruit_id` int(11) NOT NULL AUTO_INCREMENT,
  `applic_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `state` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`recruit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_recruit
-- ----------------------------
INSERT INTO `t_recruit` VALUES ('1', '1', null, '未处理');
INSERT INTO `t_recruit` VALUES ('2', '2', null, '未处理');
INSERT INTO `t_recruit` VALUES ('3', '3', null, '未处理');
INSERT INTO `t_recruit` VALUES ('4', '4', null, '未处理');
INSERT INTO `t_recruit` VALUES ('5', '5', null, '未处理');
INSERT INTO `t_recruit` VALUES ('6', '6', null, '未处理');
INSERT INTO `t_recruit` VALUES ('7', '7', null, '未处理');
INSERT INTO `t_recruit` VALUES ('8', '8', null, '未处理');
INSERT INTO `t_recruit` VALUES ('9', '9', null, '未处理');
INSERT INTO `t_recruit` VALUES ('10', '10', null, '未处理');
INSERT INTO `t_recruit` VALUES ('11', '11', null, '未处理');
INSERT INTO `t_recruit` VALUES ('12', '12', null, '未处理');
INSERT INTO `t_recruit` VALUES ('13', '13', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('14', '14', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('15', '15', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('16', '16', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('17', '17', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('18', '18', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('19', '19', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('20', '20', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('21', '21', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('22', '22', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('23', '23', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('24', '24', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('25', '25', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('26', '26', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('27', '27', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('28', '28', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('29', '29', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('30', '30', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('31', '31', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('32', '32', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('33', '33', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('34', '34', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('35', '35', null, '面试过');
INSERT INTO `t_recruit` VALUES ('36', '36', null, '面试过');
INSERT INTO `t_recruit` VALUES ('37', '37', null, '面试过');
INSERT INTO `t_recruit` VALUES ('38', '38', null, '面试过');
INSERT INTO `t_recruit` VALUES ('39', '39', null, '面试过');
INSERT INTO `t_recruit` VALUES ('40', '40', null, '面试过');
INSERT INTO `t_recruit` VALUES ('41', '41', null, '面试过');
INSERT INTO `t_recruit` VALUES ('42', '42', null, '笔试过');
INSERT INTO `t_recruit` VALUES ('43', '43', null, '面试过');
INSERT INTO `t_recruit` VALUES ('44', '44', null, '面试过');
INSERT INTO `t_recruit` VALUES ('45', '45', null, '面试过');
INSERT INTO `t_recruit` VALUES ('46', '46', null, '面试过');
INSERT INTO `t_recruit` VALUES ('47', '47', null, '面试过');
INSERT INTO `t_recruit` VALUES ('48', '48', null, '面试过');
INSERT INTO `t_recruit` VALUES ('49', '49', null, '面试过');
INSERT INTO `t_recruit` VALUES ('50', '50', null, '面试过');
INSERT INTO `t_recruit` VALUES ('51', '51', null, '面试过');
INSERT INTO `t_recruit` VALUES ('52', '52', null, '面试过');
INSERT INTO `t_recruit` VALUES ('53', '53', null, '面试过');
INSERT INTO `t_recruit` VALUES ('54', '54', null, '面试过');
INSERT INTO `t_recruit` VALUES ('55', '55', null, '面试过');
INSERT INTO `t_recruit` VALUES ('57', '57', '57', '签约完成');
INSERT INTO `t_recruit` VALUES ('58', '58', '58', '签约完成');
INSERT INTO `t_recruit` VALUES ('59', '59', '59', '签约完成');
INSERT INTO `t_recruit` VALUES ('60', '60', '60', '签约完成');
INSERT INTO `t_recruit` VALUES ('61', '61', '61', '签约完成');
INSERT INTO `t_recruit` VALUES ('62', '62', '62', '签约完成');
INSERT INTO `t_recruit` VALUES ('63', '63', '63', '签约完成');
INSERT INTO `t_recruit` VALUES ('64', '64', '64', '签约完成');
INSERT INTO `t_recruit` VALUES ('65', '65', '65', '签约完成');
INSERT INTO `t_recruit` VALUES ('66', '66', '66', '签约完成');
INSERT INTO `t_recruit` VALUES ('67', '67', '67', '签约完成');
INSERT INTO `t_recruit` VALUES ('68', '68', '68', '签约完成');
INSERT INTO `t_recruit` VALUES ('69', '69', '69', '签约完成');
INSERT INTO `t_recruit` VALUES ('70', '70', '70', '签约完成');
INSERT INTO `t_recruit` VALUES ('71', '71', '71', '签约完成');
INSERT INTO `t_recruit` VALUES ('72', '72', '72', '签约完成');
INSERT INTO `t_recruit` VALUES ('73', '73', '73', '签约完成');
INSERT INTO `t_recruit` VALUES ('74', '74', '74', '签约完成');
INSERT INTO `t_recruit` VALUES ('75', '75', '75', '签约完成');
INSERT INTO `t_recruit` VALUES ('76', '76', '76', '签约完成');
INSERT INTO `t_recruit` VALUES ('77', '77', '77', '签约完成');
INSERT INTO `t_recruit` VALUES ('78', '78', '78', '签约完成');
INSERT INTO `t_recruit` VALUES ('79', '79', '79', '签约完成');
INSERT INTO `t_recruit` VALUES ('80', '80', '80', '签约完成');
INSERT INTO `t_recruit` VALUES ('81', '81', '81', '签约完成');
INSERT INTO `t_recruit` VALUES ('82', '82', '82', '签约完成');
INSERT INTO `t_recruit` VALUES ('83', '83', '83', '签约完成');
INSERT INTO `t_recruit` VALUES ('84', '84', '84', '签约完成');
INSERT INTO `t_recruit` VALUES ('85', '85', '85', '签约完成');
INSERT INTO `t_recruit` VALUES ('86', '86', '86', '签约完成');
INSERT INTO `t_recruit` VALUES ('87', '87', '87', '签约完成');
INSERT INTO `t_recruit` VALUES ('88', '88', '88', '签约完成');
INSERT INTO `t_recruit` VALUES ('89', '89', '89', '签约完成');
INSERT INTO `t_recruit` VALUES ('90', '90', '90', '签约完成');
INSERT INTO `t_recruit` VALUES ('91', '91', '91', '签约完成');
INSERT INTO `t_recruit` VALUES ('92', '92', '92', '签约完成');
INSERT INTO `t_recruit` VALUES ('93', '93', '93', '签约完成');
INSERT INTO `t_recruit` VALUES ('94', '94', '94', '签约完成');
INSERT INTO `t_recruit` VALUES ('95', '95', '95', '签约完成');
INSERT INTO `t_recruit` VALUES ('96', '96', '96', '签约完成');
INSERT INTO `t_recruit` VALUES ('97', '97', '97', '签约完成');
INSERT INTO `t_recruit` VALUES ('98', '98', '98', '签约完成');
INSERT INTO `t_recruit` VALUES ('99', '99', '99', '签约完成');
INSERT INTO `t_recruit` VALUES ('100', '100', '100', '签约完成');

-- ----------------------------
-- Table structure for t_staff
-- ----------------------------
DROP TABLE IF EXISTS `t_staff`;
CREATE TABLE `t_staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `sex` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `birth` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(30) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `edu_back` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `section` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `duty` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `entry_time` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `state` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_staff
-- ----------------------------
INSERT INTO `t_staff` VALUES ('56', '朱野雪', '女', '2003-11-22', '13882169306', '6355368032@qq.com', '大学', '开发部', '部长', '2012-09-23', '在职');
INSERT INTO `t_staff` VALUES ('57', '江晨钰', '女', '2001-07-17', '15320025648', '4732785740@qq.com', '大学', '开发部', '部长', '2011-10-15', '在职');
INSERT INTO `t_staff` VALUES ('58', '贺雪冰', '女', '2003-12-28', '15537238675', '6840424115@qq.com', '大学', '开发部', '部长', '2012-10-12', '休假');
INSERT INTO `t_staff` VALUES ('59', '唐珑玲', '女', '2001-08-17', '13463357644', '4072833074@qq.com', '大学', '开发部', '员工', '2015-09-30', '在职');
INSERT INTO `t_staff` VALUES ('60', '彭西华', '女', '2002-12-20', '15238041575', '4325601350@qq.com', '大学', '开发部', '员工', '2010-05-01', '在职');
INSERT INTO `t_staff` VALUES ('61', '郝语风', '女', '2000-11-02', '18362177843', '4415178400@qq.com', '大学', '开发部', '员工', '2014-07-24', '在职');
INSERT INTO `t_staff` VALUES ('62', '谢婧玟', '女', '2002-10-22', '15312375950', '2686638133@qq.com', '大学', '开发部', '员工', '2010-09-05', '在职');
INSERT INTO `t_staff` VALUES ('63', '廖珉瑶', '女', '2001-12-26', '15288598767', '5131353153@qq.com', '大学', '开发部', '员工', '2010-10-25', '在职');
INSERT INTO `t_staff` VALUES ('64', '邓琼怡', '女', '2001-05-27', '18673076852', '5480435734@qq.com', '大学', '开发部', '员工', '2015-04-09', '在职');
INSERT INTO `t_staff` VALUES ('65', '朱冰蝶', '女', '2002-04-19', '15605228988', '1040007210@qq.com', '大学', '开发部', '员工', '2010-10-19', '在职');
INSERT INTO `t_staff` VALUES ('66', '宋楠楠', '女', '2002-08-01', '13593116148', '4787164472@qq.com', '大学', '行政部', '经理', '2013-04-18', '在职');
INSERT INTO `t_staff` VALUES ('67', '唐思楠', '女', '2003-01-03', '15601631789', '0082405107@qq.com', '大学', '行政部', '经理', '2010-05-26', '在职');
INSERT INTO `t_staff` VALUES ('68', '郭知世', '女', '2002-03-18', '15522305529', '1015712766@qq.com', '大学', '行政部', '经理', '2012-05-05', '在职');
INSERT INTO `t_staff` VALUES ('69', '叶冰萍', '女', '2000-08-27', '13108586104', '4603774077@qq.com', '大学', '行政部', '经理', '2011-01-19', '离职');
INSERT INTO `t_staff` VALUES ('70', '石孟乐', '女', '2000-07-23', '18536619476', '7100401250@qq.com', '大学', '行政部', '部长', '2015-02-01', '在职');
INSERT INTO `t_staff` VALUES ('71', '傅莉颖', '女', '2001-10-24', '13225018933', '4612735388@qq.com', '大学', '行政部', '部长', '2011-12-05', '在职');
INSERT INTO `t_staff` VALUES ('72', '罗歌玲', '女', '2002-09-04', '17811345820', '4560620536@qq.com', '大学', '行政部', '员工', '2014-01-10', '在职');
INSERT INTO `t_staff` VALUES ('73', '于雅香', '女', '2001-01-28', '13554809177', '4422800106@qq.com', '大学', '行政部', '员工', '2013-09-29', '在职');
INSERT INTO `t_staff` VALUES ('74', '叶从波', '女', '2003-03-09', '13470477046', '0825275654@qq.com', '大学', '行政部', '员工', '2011-02-20', '休假');
INSERT INTO `t_staff` VALUES ('75', '文秋芳', '女', '2001-04-11', '18815195864', '1117323821@qq.com', '大学', '行政部', '员工', '2012-12-04', '在职');
INSERT INTO `t_staff` VALUES ('76', '蔡凝珍', '女', '2002-01-13', '19917583233', '0578583837@qq.com', '大学', '行政部', '员工', '2012-06-01', '在职');
INSERT INTO `t_staff` VALUES ('77', '卢元英', '女', '2001-04-02', '17236506880', '2421843078@qq.com', '大学', '行政部', '员工', '2011-05-21', '在职');
INSERT INTO `t_staff` VALUES ('78', '夏小溪', '女', '2003-01-16', '19973467037', '6287433386@qq.com', '大学', '行政部', '员工', '2013-06-21', '在职');
INSERT INTO `t_staff` VALUES ('79', '唐湛恩', '女', '2003-10-02', '15235877496', '5178640302@qq.com', '大学', '行政部', '员工', '2010-04-25', '在职');
INSERT INTO `t_staff` VALUES ('80', '任春华', '女', '2001-02-28', '15545803809', '3637267887@qq.com', '大学', '行政部', '员工', '2013-10-09', '在职');
INSERT INTO `t_staff` VALUES ('81', '邹新林', '女', '2003-03-31', '18735764472', '8303475042@qq.com', '大学', '行政部', '员工', '2011-01-04', '在职');
INSERT INTO `t_staff` VALUES ('82', '高步美', '女', '2003-12-06', '19842653529', '5806115343@qq.com', '大学', '行政部', '员工', '2013-01-12', '在职');
INSERT INTO `t_staff` VALUES ('83', '文寻云', '女', '2002-04-28', '13197126828', '3805407156@qq.com', '大学', '行政部', '员工', '2015-06-20', '在职');
INSERT INTO `t_staff` VALUES ('84', '姚紫翠', '女', '2002-08-23', '15146842370', '4213521231@qq.com', '大学', '行政部', '员工', '2011-08-08', '休假');
INSERT INTO `t_staff` VALUES ('85', '谭子美', '女', '2003-06-09', '15773916086', '4340620437@qq.com', '大学', '行政部', '员工', '2014-04-21', '在职');
INSERT INTO `t_staff` VALUES ('86', '陈秀越', '女', '2003-02-06', '13862614043', '7087535650@qq.com', '大学', '行政部', '员工', '2012-06-15', '在职');
INSERT INTO `t_staff` VALUES ('87', '秦赞悦', '女', '2001-12-07', '18207001913', '1434483474@qq.com', '大学', '人力资源部', '经理', '2011-01-17', '在职');
INSERT INTO `t_staff` VALUES ('88', '武巧春', '女', '2002-11-28', '15069929678', '8336624888@qq.com', '大学', '人力资源部', '经理', '2013-10-29', '在职');
INSERT INTO `t_staff` VALUES ('89', '乔永茹', '女', '2000-06-12', '16531956874', '0185420181@qq.com', '大学', '人力资源部', '部长', '2015-09-01', '在职');
INSERT INTO `t_staff` VALUES ('90', '余怀萍', '女', '2001-02-28', '13436045611', '3154508857@qq.com', '大学', '人力资源部', '部长', '2010-12-26', '在职');
INSERT INTO `t_staff` VALUES ('91', '于醉卉', '女', '2000-03-26', '13394725936', '8468845113@qq.com', '大学', '人力资源部', '部长', '2014-06-21', '在职');
INSERT INTO `t_staff` VALUES ('92', '史依丝', '女', '2002-11-22', '15620658514', '7675804781@qq.com', '大学', '人力资源部', '部长', '2012-02-01', '离职');
INSERT INTO `t_staff` VALUES ('93', '江小枫', '女', '2000-02-26', '16516821662', '7155066816@qq.com', '大学', '人力资源部', '员工', '2015-11-21', '在职');
INSERT INTO `t_staff` VALUES ('94', '赖慧君', '女', '2002-01-04', '15832442718', '2531054060@qq.com', '大学', '人力资源部', '员工', '2014-12-11', '在职');
INSERT INTO `t_staff` VALUES ('95', '贺怡若', '女', '2002-12-24', '15276434282', '6804253045@qq.com', '大学', '人力资源部', '员工', '2015-03-15', '在职');
INSERT INTO `t_staff` VALUES ('96', '贾怡宁', '女', '2003-06-16', '15594936823', '5183868071@qq.com', '大学', '人力资源部', '员工', '2010-11-30', '在职');
INSERT INTO `t_staff` VALUES ('97', '王静曼', '女', '2000-07-01', '13434393090', '6684122653@qq.com', '大学', '人力资源部', '员工', '2012-03-04', '在职');
INSERT INTO `t_staff` VALUES ('98', '梁艳霞', '女', '2000-09-20', '13489539500', '5418471134@qq.com', '大学', '人力资源部', '员工', '2012-02-13', '在职');
INSERT INTO `t_staff` VALUES ('99', '郭和静', '女', '2000-06-14', '13920717234', '3635106013@qq.com', '大学', '人力资源部', '员工', '2014-09-08', '在职');
INSERT INTO `t_staff` VALUES ('100', '宋琴心', '女', '2001-03-07', '17363503585', '6314288530@qq.com', '大学', '人力资源部', '员工', '2011-11-07', '休假');
INSERT INTO `t_staff` VALUES ('102', '111', '男', '2022-12-01', '111', '111', '本科', '销售部', '111', '2022-12-19', '在职');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `state` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('1', 'lx', 'lx', '在线', '1798903906@qq.com');
INSERT INTO `t_user` VALUES ('2', 'zxy', '123', '在线', '2825033020@qq.com');
INSERT INTO `t_user` VALUES ('3', 'lj', 'lj', null, 'lj');
INSERT INTO `t_user` VALUES ('4', '111', '111', '离线', '2749027218@qq.com');
