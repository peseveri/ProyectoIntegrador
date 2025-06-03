-- 1. Crear la base de datos
DROP DATABASE IF EXISTS sales_company;
CREATE DATABASE IF NOT EXISTS sales_company;
USE sales_company;


-- 2. Crear las tablas

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
	CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(45)
);

DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
	CountryID INT PRIMARY KEY,
    CountryName VARCHAR(100),
    CountryCode VARCHAR(10)
);

DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
	CityID INT PRIMARY KEY,
    CityName VARCHAR(45),
    Zipcode VARCHAR(10),
    CountryID INT
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
	CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    MiddleInital VARCHAR(5),
	LastName VARCHAR(100),
    CityID INT,
    Address VARCHAR(225)
);

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
	EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    MiddleInital CHAR(1),
	LastName VARCHAR(100),
    BirthDate DATETIME,
    Gender CHAR(1),
	CityID INT,
    HireDate DATETIME
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
	ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10,4),
	CategoryID INT,
    Class VARCHAR(50),
    ModifyDate TIME,
	Resistant VARCHAR(50),
    IsAllergic VARCHAR(10),
    VitalityDays INT
);

DROP TABLE IF EXISTS sales;
CREATE TABLE sales (
	SalesID INT PRIMARY KEY,
    SalesPersonID INT,
    CustomerId INT,
	ProducID INT,
    Quantity TIME,
	Discount DECIMAL(4,2),
    TotalPrice DECIMAL(10,2),
    SalesDate TIME,
    TransactionNumber VARCHAR(50)
);


-- 3. Cargar los datos desde los archivos CSV
SHOW VARIABLES LIKE 'secure_file_priv';  -- veo la ruta en donde debo dejar los csv para que se puedan cargar exitosamente

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/categories.csv'
INTO TABLE categories
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/countries.csv'
INTO TABLE countries
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cities.csv'
INTO TABLE cities
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

