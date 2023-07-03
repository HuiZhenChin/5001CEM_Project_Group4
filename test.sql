-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 03, 2023 at 09:46 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `addedtraining`
--

CREATE TABLE `addedtraining` (
  `AID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `TID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `DATE` varchar(20) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `NAME` varchar(50) CHARACTER SET latin1 NOT NULL,
  `PHONE` varchar(15) CHARACTER SET latin1 NOT NULL,
  `EMAIL` varchar(50) CHARACTER SET latin1 NOT NULL,
  `DEPARTMENT` varchar(15) CHARACTER SET latin1 NOT NULL,
  `PROFILE_PIC` longblob NOT NULL,
  `PASSWORD` varchar(1000) CHARACTER SET latin1 NOT NULL,
  `SALT` varchar(100) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `approved`
--

CREATE TABLE `approved` (
  `TID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `SID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `HID` varchar(4) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `completed`
--

CREATE TABLE `completed` (
  `TITLE` varchar(50) CHARACTER SET latin1 NOT NULL,
  `ID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `DATE` varchar(15) CHARACTER SET latin1 NOT NULL,
  `TIME` varchar(15) CHARACTER SET latin1 NOT NULL,
  `VENUE` varchar(30) CHARACTER SET latin1 NOT NULL,
  `COST` varchar(10) CHARACTER SET latin1 NOT NULL,
  `IMAGE` longblob NOT NULL,
  `DEPARTMENT` varchar(30) CHARACTER SET latin1 DEFAULT NULL,
  `DESCRIPTION` varchar(1000) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `done`
--

CREATE TABLE `done` (
  `TID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `SID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `HID` varchar(4) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `edittraining`
--

CREATE TABLE `edittraining` (
  `AID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `TID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `DATE` varchar(20) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `hrassistant`
--

CREATE TABLE `hrassistant` (
  `ID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `NAME` varchar(50) CHARACTER SET latin1 NOT NULL,
  `PHONE` varchar(15) CHARACTER SET latin1 NOT NULL,
  `EMAIL` varchar(50) CHARACTER SET latin1 NOT NULL,
  `DEPARTMENT` varchar(15) CHARACTER SET latin1 NOT NULL,
  `PROFILE_PIC` longblob NOT NULL,
  `PASSWORD` varchar(1000) CHARACTER SET latin1 NOT NULL,
  `SALT` varchar(100) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ongoing`
--

CREATE TABLE `ongoing` (
  `TITLE` varchar(50) CHARACTER SET latin1 NOT NULL,
  `ID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `DATE` varchar(15) CHARACTER SET latin1 NOT NULL,
  `TIME` varchar(15) CHARACTER SET latin1 NOT NULL,
  `VENUE` varchar(30) CHARACTER SET latin1 NOT NULL,
  `COST` varchar(10) CHARACTER SET latin1 NOT NULL,
  `IMAGE` longblob NOT NULL,
  `DEPARTMENT` varchar(30) CHARACTER SET latin1 DEFAULT NULL,
  `DESCRIPTION` varchar(1000) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `registered`
--

CREATE TABLE `registered` (
  `TID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `SID` varchar(4) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rejected`
--

CREATE TABLE `rejected` (
  `TID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `SID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `HID` varchar(4) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `removetraining`
--

CREATE TABLE `removetraining` (
  `AID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `RMVDATE` varchar(30) CHARACTER SET latin1 NOT NULL,
  `TITLE` varchar(50) CHARACTER SET latin1 NOT NULL,
  `TID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `DATE` varchar(15) CHARACTER SET latin1 NOT NULL,
  `TIME` varchar(15) CHARACTER SET latin1 NOT NULL,
  `VENUE` varchar(30) CHARACTER SET latin1 NOT NULL,
  `COST` varchar(10) CHARACTER SET latin1 NOT NULL,
  `IMAGE` longblob NOT NULL,
  `DEPARTMENT` varchar(30) CHARACTER SET latin1 DEFAULT NULL,
  `DESCRIPTION` varchar(1000) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `ID` varchar(4) CHARACTER SET latin1 NOT NULL,
  `NAME` varchar(50) CHARACTER SET latin1 NOT NULL,
  `PHONE` varchar(15) CHARACTER SET latin1 NOT NULL,
  `EMAIL` varchar(50) CHARACTER SET latin1 NOT NULL,
  `DEPARTMENT` varchar(15) CHARACTER SET latin1 NOT NULL,
  `PROFILE_PIC` longblob NOT NULL,
  `PASSWORD` varchar(1000) CHARACTER SET latin1 NOT NULL,
  `SALT` varchar(100) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `training`
--

CREATE TABLE `training` (
  `TITLE` varchar(50) CHARACTER SET latin1 NOT NULL,
  `ID` varchar(5) CHARACTER SET latin1 NOT NULL,
  `DATE` varchar(15) CHARACTER SET latin1 NOT NULL,
  `TIME` varchar(15) CHARACTER SET latin1 NOT NULL,
  `VENUE` varchar(30) CHARACTER SET latin1 NOT NULL,
  `COST` varchar(10) CHARACTER SET latin1 NOT NULL,
  `IMAGE` longblob NOT NULL,
  `DEPARTMENT` varchar(30) CHARACTER SET latin1 DEFAULT NULL,
  `DESCRIPTION` varchar(1000) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
