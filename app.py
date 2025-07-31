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
    

@app.route('/stats',methods=['GET','POST'])
def stats():
    completed_books = 0
    to_read_books = 0
    read_books = 0
    total_pages_read = 0
    status = db.execute("SELECT completion_status as s,pages as p FROM books")
    print(status)
    for dict in status:
        if dict['s'] == 'completed':
            completed_books+=1
            total_pages_read+=dict['p']
        elif dict['s'] == 'to-read':
            to_read_books+=1
        elif dict['s'] == 'read':
            read_books+=1
            
    return render_template("stats.html",completed_books=completed_books,to_read_books=to_read_books,read_books=read_books,total_pages_read=total_pages_read)


@app.route("/about",methods=["GET","POST"])
def about():
    return render_template("about.html")