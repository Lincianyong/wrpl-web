-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 25, 2024 at 01:37 AM
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
-- Database: `ecommerce`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customerID` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customerID`, `name`, `address`) VALUES
('C001', 'John Doe', '123 Main Street'),
('C002', 'Alice Smith', '456 Elm Street'),
('C003', 'Bob Johnson', '789 Oak Avenue'),
('C004', 'Emily Brown', '101 Pine Road'),
('C005', 'David Wilson', '202 Maple Lane'),
('C006', 'Sarah Jones', '303 Cedar Street'),
('C007', 'Michael Davis', '404 Birch Drive'),
('C008', 'Emma Taylor', '505 Willow Court'),
('C009', 'Christopher Martinez', '606 Pineapple Avenue'),
('C010', 'Olivia Rodriguez', '707 Elmwood Lane'),
('C011', 'William Hernandez', '808 Oakwood Drive'),
('C012', 'Sophia Lopez', '909 Cedar Avenue'),
('C013', 'James Gonzalez', '1010 Maple Road'),
('C014', 'Isabella Perez', '1111 Pinecrest Boulevard'),
('C015', 'Alexander Torres', '1212 Willow Street'),
('C016', 'Mia Rivera', '1313 Oakcrest Avenue'),
('C017', 'Daniel Moore', '1414 Cedar Lane'),
('C018', 'Charlotte Sanchez', '1515 Elm Drive'),
('C019', 'Benjamin Bennett', '1616 Oakwood Court'),
('C020', 'Ava Powell', '1717 Maple Avenue');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `productID` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `seller` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`productID`, `name`, `price`, `stock`, `seller`, `description`) VALUES
('P00-001', 'Smart TV 55\"', 8500000, 25, 'Jabberstorm', 'Experience stunning visuals with this 55-inch Smart TV. Enjoy streaming your favorite content.'),
('P00-002', 'Laptop - Core i7', 15000000, 15, 'Voonder', 'High-performance laptop powered by Intel Core i7 processor. Ideal for work and gaming.'),
('P00-003', 'Smartphone - X10', 7200000, 30, 'Tekfly', 'The latest smartphone model featuring a powerful camera, fast processor, and sleek design.'),
('P00-004', 'Wireless Headphones', 1500000, 50, 'Kayveo', 'Enjoy your music without the hassle of tangled wires. These wireless headphones offer crisp sound.'),
('P00-005', 'Gaming Console', 6000000, 20, 'Jabberstorm', 'Immerse yourself in the world of gaming with this advanced gaming console.'),
('P00-006', 'Drone - Pro', 12500000, 10, 'Voonder', 'Capture breathtaking aerial footage with this professional-grade drone.'),
('P00-007', 'Smart Watch', 3000000, 40, 'Tekfly', 'Stay connected and track your fitness goals with this sleek smartwatch.'),
('P00-008', 'Bluetooth Speaker', 800000, 60, 'Kayveo', 'Portable speaker with Bluetooth connectivity, perfect for parties and outdoor adventures.'),
('P00-009', 'DSLR Camera', 10000000, 12, 'Jabberstorm', 'Capture life\'s moments in stunning detail with this high-quality DSLR camera.'),
('P00-010', 'Tablet - iPad Air', 9500000, 18, 'Voonder', 'Slim and powerful tablet with a vibrant display, perfect for work and entertainment.'),
('P00-011', 'Desktop PC', 12000000, 8, 'Tekfly', 'High-performance desktop PC suitable for gaming, design, and multimedia tasks.'),
('P00-012', 'VR Headset', 3800000, 25, 'Kayveo', 'Dive into immersive virtual worlds with this cutting-edge VR headset.'),
('P00-013', 'Home Theater System', 9000000, 15, 'Jabberstorm', 'Create a cinematic experience at home with this powerful home theater system.'),
('P00-014', 'Action Camera', 2200000, 35, 'Voonder', 'Record your adventures in stunning 4K resolution with this compact action camera.'),
('P00-015', 'Wireless Router', 1200000, 40, 'Tekfly', 'Ensure fast and stable internet connectivity with this high-speed wireless router.'),
('P00-016', 'Smart Thermostat', 1700000, 20, 'Kayveo', 'Control your home\'s temperature from anywhere with this smart thermostat.'),
('P00-017', 'E-book Reader', 900000, 45, 'Jabberstorm', 'Carry thousands of books in your pocket with this lightweight e-book reader.'),
('P00-018', 'Portable Projector', 4500000, 10, 'Voonder', 'Turn any space into a movie theater with this portable projector.'),
('P00-019', 'Fitness Tracker', 750000, 55, 'Tekfly', 'Monitor your daily activity and improve your fitness with this handy tracker.'),
('P00-020', 'Wireless Earbuds', 1200000, 30, 'Kayveo', 'Enjoy wireless freedom and premium sound quality with these sleek earbuds.');

-- --------------------------------------------------------

--
-- Table structure for table `shippings`
--

CREATE TABLE `shippings` (
  `shippingID` varchar(255) NOT NULL,
  `companyName` varchar(255) DEFAULT NULL,
  `fee` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shippings`
--

INSERT INTO `shippings` (`shippingID`, `companyName`, `fee`) VALUES
('S001', 'FastShip', 8000),
('S002', 'SwiftDelivery', 7000),
('S003', 'QuickShip', 6000),
('S004', 'RapidTransit', 5500),
('S005', 'ExpressShip', 6500);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `transactionID` varchar(255) NOT NULL,
  `transactionDate` date DEFAULT NULL,
  `transactionStatus` varchar(50) DEFAULT NULL,
  `transactionPrice` int(11) DEFAULT NULL,
  `customerID` varchar(255) DEFAULT NULL,
  `shippingID` varchar(255) DEFAULT NULL,
  `productID` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`transactionID`, `transactionDate`, `transactionStatus`, `transactionPrice`, `customerID`, `shippingID`, `productID`) VALUES
('T001', '2024-03-20', 'Completed', 8500000, 'C001', 'S001', 'P00-001'),
('T002', '2024-03-20', 'Pending', 15000000, 'C002', 'S002', 'P00-002'),
('T003', '2024-03-21', 'Completed', 7200000, 'C003', 'S003', 'P00-003'),
('T004', '2024-03-21', 'Pending', 1500000, 'C004', 'S004', 'P00-004'),
('T005', '2024-03-22', 'Completed', 6000000, 'C005', 'S005', 'P00-005'),
('T006', '2024-03-22', 'Completed', 12500000, 'C006', 'S001', 'P00-006'),
('T007', '2024-03-23', 'Pending', 3000000, 'C007', 'S002', 'P00-007'),
('T008', '2024-03-23', 'Completed', 800000, 'C008', 'S003', 'P00-008'),
('T009', '2024-03-24', 'Pending', 10000000, 'C009', 'S004', 'P00-009'),
('T010', '2024-03-24', 'Completed', 9500000, 'C010', 'S005', 'P00-010'),
('T011', '2024-03-25', 'Pending', 12000000, 'C011', 'S001', 'P00-011'),
('T012', '2024-03-25', 'Completed', 3800000, 'C012', 'S002', 'P00-012'),
('T013', '2024-03-26', 'Pending', 9000000, 'C013', 'S003', 'P00-013'),
('T014', '2024-03-26', 'Completed', 2200000, 'C014', 'S004', 'P00-014'),
('T015', '2024-03-27', 'Pending', 1200000, 'C015', 'S005', 'P00-015');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customerID`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`productID`);

--
-- Indexes for table `shippings`
--
ALTER TABLE `shippings`
  ADD PRIMARY KEY (`shippingID`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`transactionID`),
  ADD KEY `customerID` (`customerID`),
  ADD KEY `shippingID` (`shippingID`),
  ADD KEY `productID` (`productID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customers` (`customerID`),
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`shippingID`) REFERENCES `shippings` (`shippingID`),
  ADD CONSTRAINT `transactions_ibfk_3` FOREIGN KEY (`productID`) REFERENCES `products` (`productID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
