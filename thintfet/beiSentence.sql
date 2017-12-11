-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 29, 2016 at 05:56 AM
-- Server version: 5.5.47-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `beiSentence`
--

-- --------------------------------------------------------

--
-- Table structure for table `analysis`
--

CREATE TABLE IF NOT EXISTS `analysis` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `user` varchar(200) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sentence` varchar(500) CHARACTER SET utf8 NOT NULL,
  `result` int(11) NOT NULL,
  `answer` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `analysis`
--

INSERT INTO `analysis` (`id`, `user`, `time`, `sentence`, `result`, `answer`) VALUES
(4, 'Jiayan Zhu', '2016-02-24 05:17:31', 'haha', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `pages`
--

CREATE TABLE IF NOT EXISTS `pages` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `user` mediumint(9) NOT NULL,
  `title` varchar(200) NOT NULL,
  `header` varchar(300) NOT NULL,
  `body` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `pages`
--

INSERT INTO `pages` (`id`, `user`, `title`, `header`, `body`) VALUES
(1, 0, 'Home Page', '欢迎来到被字句分析网站(Welcome to Bei Sentence Analyser)', '网站概述(Summary of this website)'),
(5, 0, 'About me', '我的简历(About me)', '我是复旦大学对外汉语专业的研究生'),
(6, 0, 'Analysis', '被字句分析(Bei Sentence Analyser)', '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `first` varchar(200) NOT NULL,
  `last` varchar(200) NOT NULL,
  `email` varchar(300) NOT NULL,
  `password` varchar(200) NOT NULL,
  `status` int(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `first`, `last`, `email`, `password`, `status`) VALUES
(1, 'Guest', 'User', 'user@user.com', '37fa265330ad83eaa879efb1e2db6380896cf639', 1),
(2, 'Jiayan', 'Zhu', 'jiayanzhu_judy@163.com', '6298a74ea665b619983142da0ca6db475c43432a', 1),
(3, 'Mingda', 'Li', 'ml888@cornell.edu', 'acbc301f45bc859c76290bd1c9764a2a7c93480e', 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
