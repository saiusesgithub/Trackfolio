from cs50 import SQL
from flask import Flask,render_template,request,redirect

app = Flask(__name__)
db = SQL("sqlite:///trackfolio.db")

@app.route("/",methods=["GET","POST"])
def index(): 
    return render_template("index.html")

@app.route("/dashboard",methods=["GET","POST"])
def dashboard(): 
    # sort by reading first then read then to read
    books = db.execute("SELECT * FROM books")
    return render_template("dashboard.html",books=books)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "POST":
        db.execute("INSERT INTO books (title,author,pages,completion_status,date_start,date_end,genre,rating) VALUES (?,?,?,?,?,?,?,?)",request.form.get("title"),request.form.get("author"),request.form.get("pages"),request.form.get("completion_status"),request.form.get("date_start"),request.form.get("date_end"),request.form.get("genre"),request.form.get("rating"))
        return redirect("/dashboard")
    else:
        return render_template("add.html")
    

@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id):
    if request.method == "POST":
        db.execute("UPDATE books SET title = ?, author = ?, pages = ?, completion_status = ? ,date_start = ? ,date_end = ?, genre = ? ,rating = ? WHERE id = ?",request.form.get("title"),request.form.get("author"),request.form.get("pages"),request.form.get("completion_status"),request.form.get("date_start"),request.form.get("date_end"),request.form.get("genre"),request.form.get("rating"),id)
        return redirect("/dashboard")
    else:
        book =db.execute("SELECT * FROM books WHERE id= ?",id)[0]
        return render_template("edit.html",book = book)
    

@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    if request.method == "POST":
        db.execute("DELETE FROM books WHERE id = ?",id)
        return redirect("/dashboard")
    else:
        book = db.execute("SELECT * FROM books WHERE id= ?",id)[0]
        return render_template("delete.html",book = book)

