from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select database
db = client["MiniBookShelf"]

# Select collection
books = db["books"]


# Home page - display all books
@app.route("/")
def home():

    search = request.args.get("search", "")

    if search:
        all_books = books.find({
            "title": {
                "$regex": search,
                "$options": "i"
            }
        })
    else:
        all_books = books.find()

    return render_template("index.html", books=all_books, search=search)


# Add a new book
@app.route("/add", methods=["POST"])
def add_book():

    title = request.form["title"]
    author = request.form["author"]
    category = request.form["category"]
    year = request.form["year"]
    price = request.form["price"]

    book = {
        "title": title,
        "author": author,
        "category": category,
        "year": int(year),
        "price": float(price)
    }

    books.insert_one(book)

    return redirect("/")


# Delete a book
@app.route("/delete/<book_id>")
def delete_book(book_id):

    books.delete_one({
        "_id": ObjectId(book_id)
    })

    return redirect("/")


# Edit book page
@app.route("/edit/<book_id>")
def edit_book(book_id):

    book = books.find_one({
        "_id": ObjectId(book_id)
    })

    return render_template("edit.html", book=book)


# Update book
@app.route("/update/<book_id>", methods=["POST"])
def update_book(book_id):

    title = request.form["title"]
    author = request.form["author"]
    category = request.form["category"]
    year = request.form["year"]
    price = request.form["price"]

    books.update_one(
        {"_id": ObjectId(book_id)},
        {
            "$set": {
                "title": title,
                "author": author,
                "category": category,
                "year": int(year),
                "price": float(price)
            }
        }
    )

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=False)