from cs50 import SQL
from flask import Flask,render_template,request,redirect

app = Flask(__name__)
db = SQL("sqlite:///trackfolio.db")

@app.route("/",methods=["GET","POST"])
def dashboard(): 
    # sort by reading first then read then to read
    books = db.execute("SELECT * FROM books")
    return render_template("dashboard.html",books=books)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "POST":
        db.execute("INSERT INTO books (title,author,pages,completion_status,date_start,date_end,genre,rating) VALUES (?,?,?,?,?,?,?,?)",request.form.get("title"),request.form.get("author"),request.form.get("pages"),request.form.get("completion_status"),request.form.get("date_start"),request.form.get("date_end"),request.form.get("genre"),request.form.get("rating"))
        return redirect("/")
    else:
        return render_template("add.html")

