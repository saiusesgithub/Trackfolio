# 📚 Trackfolio – Book Tracker App

**A minimal, personal book-tracking web app built using Flask, Jinja, Bootstrap, and SQLite.**

---

### 🌐 Hosted Live At:

[Render](https://trackfolio-1aao.onrender.com/)

---

## 🧠 About This Project

**Trackfolio** is a lightweight book tracker built as the **final project for CS50x**. What makes it special? It was **fully built in just one day** from scratch — everything from routing to styling.

It lets you:

* Add, edit, and delete books
* Track reading status (completed, reading, to-read)
* View basic stats (books read, total pages, etc.)
* Store details like author, genre, date, and personal rating

The goal: a simple, efficient, no-frills app to track my reading journey. Built with clarity in mind, and intentionally minimal.

---

## 🛠️ Technologies Used

| Layer      | Tech Stack             |
| ---------- | ---------------------- |
| Front End  | HTML, CSS, Bootstrap 5 |
| Back End   | Flask, Jinja2 (Python) |
| Database   | SQLite                 |
| Deployment | Render.com             |

---

## 📁 Project Structure

```
Trackfolio--CS50-final-project/
├── app.py               # Flask app with routes and logic
├── templates/           # HTML files (Jinja2 templating)
│   ├── layout.html
│   ├── dashboard.html
│   ├── add.html
│   ├── edit.html
│   ├── delete.html
│   ├── stats.html
│   └── about.html
├── static/              # (Optional) Add custom CSS, images
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it :)
```

---

## 📈 Features

* ✅ Add and manage your books
* 📊 View basic reading stats
* 📝 Editable forms with prefilled data
* 🪩 Confirm before deletion
* 🌟 Responsive UI with Bootstrap
* 📄 SQLite storage — simple and file-based

---

## 💭 Design Notes

* Intentionally kept minimal and direct
* Focused more on functionality than flashy UI
* Entire structure written by hand (no generators or AI)
* Fully responsive, works on mobile too

---

## 🚀 Future Improvements

* User login system
* Book cover upload or external API integration
* Graphs for detailed reading trends
* Dark mode / themes

---

## 🚗 Deployment

App is hosted live at:
👉 [Render](https://trackfolio-1aao.onrender.com/)

To run locally:

```bash
$ git clone https://github.com/saiusesgithub/Trackfolio
$ cd Trackfolio
$ pip install -r requirements.txt
$ flask run
```

---

## 🧑‍💻 Author

**Sai Srujan**
2nd Year IT Student @ VJIT
Made as CS50x Final Project 2025
✨ Entire project made in one day
🖐 No AI used. Everything handwritten.
