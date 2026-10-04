# 📚 Mini Book Shelf

A simple web-based **Mini Book Shelf application** developed using **Python Flask and MongoDB**. The application allows users to manage their personal collection of books through a simple and user-friendly interface.

## 🎯 Project Objective

The main objective of this project is to implement a basic **Book Management System** using MongoDB as a NoSQL database.

The application provides CRUD operations to:

- Add books
- View books
- Search books
- Update book details
- Delete books

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Frontend structure |
| CSS | Website styling |
| Python | Backend programming |
| Flask | Web framework |
| MongoDB | Database |
| PyMongo | MongoDB connection |
| VS Code | Development environment |

## ✨ Features

### ➕ Add Book
Users can add a new book by entering:

- Book Title
- Author
- Category
- Publication Year
- Price

### 📖 View Books
All books stored in the MongoDB database are displayed on the home page.

### 🔍 Search Books
Users can search for books by entering the book title.

### ✏️ Update Book
Existing book details can be edited and updated.

### 🗑️ Delete Book
Users can delete books from the collection.

## 🗄️ Database

**Database Name:**

```text
MiniBookShelf
```

**Collection Name:**

```text
books
```

Each book contains:

```text
{
    title,
    author,
    category,
    year,
    price
}
```

MongoDB automatically generates a unique `_id` for each book.

## 📂 Project Structure

```text
MiniBookShelf/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── edit.html
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kamakshi1nov-cmyk/MiniBookShelf.git
```

### 2. Open the Project

```bash
cd MiniBookShelf
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Start MongoDB

Make sure MongoDB is installed and running on your computer.

The application connects to:

```text
mongodb://localhost:27017/
```

### 7. Run the Flask Application

```bash
python app.py
```

### 8. Open in Browser

Open:

```text
http://127.0.0.1:5000/
```

## 🔄 Application Workflow

```text
User
  ↓
HTML + CSS Interface
  ↓
Flask Backend
  ↓
PyMongo
  ↓
MongoDB
  ↓
Book Data
```

## 📌 CRUD Operations

| Operation | Function |
|---|---|
| Create | Add a new book |
| Read | View and search books |
| Update | Edit existing book details |
| Delete | Remove a book |

## 🎓 Academic Project

**Course:** Big Data Analytics  
**Project:** Implementation of a Mini Book Shelf using MongoDB  
**Semester:** VII  
**Department:** Computer Science and Engineering  

## 👩‍💻 Developer

**K. Kamakshi Shenoy**

Computer Science and Engineering  
Canara Engineering College

## 📜 License

This project is created for **academic and educational purposes**.