-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 03:37 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `Class_Name` varchar(30) NOT NULL,
  `Student_ID` varchar(10) NOT NULL,
  `Status` varchar(30) NOT NULL,
  `Absent` varchar(100) NOT NULL,
  `Total_Student` varchar(100) NOT NULL,
  `Present` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`Class_Name`, `Student_ID`, `Status`, `Absent`, `Total_Student`, `Present`) VALUES
('Zuhal', '2020764345', 'Absent', '2', '10', '8'),
('Musytari', '2020246301', 'Present', '3', '15', '12'),
('Zuhal', '2020571991', 'Present', '2', '10', '8'),
('Zuhal', '2020101257', 'Absent', '2', '11', '9'),
('Marikh', '2020347801', 'Present', '4', '20', '16');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
