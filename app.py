from flask import Flask, render_template, flash, request, redirect, session, abort
import re
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_reference")
def add_reference():
   return render_template("add_reference.html")

@app.route("/create_reference", methods=["POST"])
def create_reference():

    title = request.form["title"].strip()
    if len(title) > 50 or not title:
        flash("Error: Title must be between 1 and 50 letters")
        return redirect("/add_image")
    author = request.form["author"].strip()
    if len(author) > 50 or not author:
        flash("Error: Author must be between 1 and 50 letters")
        return redirect("/add_reference")

    year = request.form["year"]
    if not re.search("^[1-2][0-9]{3}$", year):
        flash("Error: Focal length must be between 1mm and 999 mm")
        return redirect("/add_image")

    ### To implement
    #try:
    #    references.add_reference(title, author, year)
    #except sqlite3.IntegrityError:
    #    return "Already exists"

    return redirect("/")
