# Library Management System API

## Project Overview

This project implements a web application for managing a library system using FastAPI. The system allows library administrators to manage books, members, and borrowing records, all while interacting with a MySQL database. The backend supports various operations, such as adding, viewing, and managing books, members, and borrowings.

## Features

- **CRUD Operations:**
  - **Books:** Add, update, delete, and view book records.
  - **Members:** Add, update, delete, and view member records.
  - **Borrow Records:** Record and manage borrowing activities, linking books to members.
  
- **Data Validation:** Pydantic models ensure the validation of data for incoming requests and outgoing responses.
  
- **Error Handling:** The system provides detailed error messages for issues like missing records or database connection failures.
  
- **API Endpoints:**
  - `/books/` - Manage book records.
  - `/members/` - Manage member records.
  - `/borrow/` - Manage borrow records.

## Database Structure

The project utilizes the `library_management` MySQL database, which consists of three main tables:
- **Books:** Stores information about books, including the title, genre, author, publication year, and price.
- **Members:** Stores details about library members, including their first and last name, email, phone number, and membership date.
- **Borrowings:** Tracks borrowing activities, linking members to the books they borrow and managing the borrow and return dates.

The SQL script to create the database and tables is as follows:

```sql
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
```

# 📚 Library Management System - Setup Guide

Welcome to the Library Management System powered by **FastAPI** and **MySQL**. This guide will help you set up the project quickly.

---

## 🚀 Setup Instructions

### 1. Set up the Database
Import the `library_management.sql` file into your MySQL server to create the necessary database tables.

---

### 2. Install Dependencies

#### Step 1: Create a virtual environment
```bash
python -m venv venv
```

#### Step 2: Activate the virtual environment

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

#### Step 3: Install dependencies

If you have a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

Or manually install the key dependencies:
```bash
pip install fastapi mysql-connector-python
```

---

## 📦 Dependencies

- **FastAPI** – A modern, high-performance web framework for building APIs with Python.
- **MySQL Connector** – Python driver to connect and interact with MySQL databases.

---

## 🧪 Testing the API

After starting the FastAPI server, go to:

```bash
http://127.0.0.1:8000/docs
```

This opens the interactive API documentation where you can explore and test all available endpoints.

---

## 🤝 Contributing

Have ideas or improvements? Feel free to fork the repository, make your changes, and open a pull request. Contributions are welcome!

---

## 🙏 Acknowledgements

- 💡 [FastAPI](https://fastapi.tiangolo.com/) for enabling rapid API development.
- 🗃️ [MySQL](https://www.mysql.com/) for providing a robust, scalable database engine.

---

Crafted for efficient knowledge systems — because organizing books should be as smooth as streaming data from a sensor.
