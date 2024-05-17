
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(50),
    Price DECIMAL(10,2)
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE,
    Name VARCHAR(50),
    Department VARCHAR(50)
);



CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(50),
    Price DECIMAL(10,2),
    StockQuantity INT,
    CHECK (StockQuantity >= 0)
);



CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    HireDate DATE NOT NULL,
    Department VARCHAR(50)
);