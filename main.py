from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management API!"}

# Database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SamSha1M$",
            database="library_management"
        )
        return connection
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")

# -------------------- MODELS --------------------

# Book models
class Book(BaseModel):
    book_id: Optional[int] = None
    title: str
    isbn: str
    category_id: int
    publisher_id: int
    publication_year: int
    copies_available: int

class BookCreate(BaseModel):
    title: str
    isbn: str
    category_id: int
    publisher_id: int
    publication_year: int
    copies_available: int

# Member models
class Member(BaseModel):
    member_id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    join_date: str

class MemberCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    join_date: str

# Borrow model
class BorrowRecord(BaseModel):
    record_id: Optional[int] = None
    book_id: int
    member_id: int
    borrow_date: str
    return_date: Optional[str] = None

class BorrowCreate(BaseModel):
    book_id: int
    member_id: int
    borrow_date: str
    return_date: Optional[str] = None

# -------------------- BOOK ROUTES --------------------

@app.post("/books/", response_model=Book)
def create_book(book: BookCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
        INSERT INTO books (title, isbn, category_id, publisher_id, publication_year, copies_available)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (book.title, book.isbn, book.category_id, book.publisher_id, book.publication_year, book.copies_available))
        connection.commit()
        book_id = cursor.lastrowid
        return {**book.dict(), "book_id": book_id}
    except Error as e:
        raise HTTPException(status_code=400, detail=f"Error creating book: {e}")
    finally:
        cursor.close()
        connection.close()

@app.get("/books/", response_model=List[Book])
def read_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Error fetching books: {e}")
    finally:
        cursor.close()
        connection.close()

# -------------------- MEMBER ROUTES --------------------

@app.post("/members/", response_model=Member)
def create_member(member: MemberCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
        INSERT INTO members (first_name, last_name, email, phone, join_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (member.first_name, member.last_name, member.email, member.phone, member.join_date))
        connection.commit()
        member_id = cursor.lastrowid
        return {**member.dict(), "member_id": member_id}
    except Error as e:
        raise HTTPException(status_code=400, detail=f"Error creating member: {e}")
    finally:
        cursor.close()
        connection.close()

@app.get("/members/", response_model=List[Member])
def read_members():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM members")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Error fetching members: {e}")
    finally:
        cursor.close()
        connection.close()

# -------------------- BORROW RECORD ROUTES --------------------

@app.post("/borrow/", response_model=BorrowRecord)
def borrow_book(record: BorrowCreate):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
        INSERT INTO borrow_records (book_id, member_id, borrow_date, return_date)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (record.book_id, record.member_id, record.borrow_date, record.return_date))
        connection.commit()
        record_id = cursor.lastrowid
        return {**record.dict(), "record_id": record_id}
    except Error as e:
        raise HTTPException(status_code=400, detail=f"Error creating borrow record: {e}")
    finally:
        cursor.close()
        connection.close()

@app.get("/borrow/", response_model=List[BorrowRecord])
def get_borrow_records():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM borrow_records")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Error fetching records: {e}")
    finally:
        cursor.close()
        connection.close()
