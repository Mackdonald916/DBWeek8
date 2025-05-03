-- Create Database
CREATE DATABASE library_management;
USE library_management;

-- Create Tables

-- Books Table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publication_year YEAR NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0)
);

-- Members Table
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    membership_date DATE NOT NULL
);

-- Borrowings Table (Many-to-Many relationship between Books and Members)
CREATE TABLE borrowings (
    borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Insert Data
-- Books
INSERT INTO books (title, genre, author, publication_year, price) VALUES
('To Kill a Mockingbird', 'Fiction', 'Harper Lee', 1960, 15.99),
('1984', 'Dystopian', 'George Orwell', 1949, 12.50),
('Sapiens: A Brief History of Humankind', 'Non-Fiction', 'Yuval Noah Harari', 2011, 18.00);

-- Members
INSERT INTO members (first_name, last_name, email, phone, membership_date) VALUES
('Alice', 'Johnson', 'alice@outlook.com', '0701238020', '2023-02-10'),
('Brian', 'Smith', 'brian@gmail.com', '0785179495', '2023-04-15'),
('Clara', 'Wright', 'clara@yahoo.com', '0714525354', '2023-07-20');

-- Borrowings
INSERT INTO borrowings (book_id, member_id, borrow_date, return_date) VALUES
(1, 1, '2025-04-01', '2025-04-10'),
(2, 2, '2025-04-10', '2025-04-17'),
(3, 3, '2025-04-15', NULL);  -- NULL means not yet returned

-- Basic Query to Verify Data
SELECT b.title, b.genre, m.first_name, m.last_name, br.borrow_date, br.return_date
FROM borrowings br
JOIN books b ON br.book_id = b.book_id
JOIN members m ON br.member_id = m.member_id;
