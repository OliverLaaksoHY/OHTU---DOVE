from flask import Flask, render_template, flash, request, redirect, session, abort
import sqlite3
import utils
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
    author = request.form["author"].strip()

    year = request.form["year"]
    
    try:
        utils.validate_text_entries([("title", title), ("author", author)])
        utils.validate_year_entry(year)
        ### function call that adds the reference entry to the database 
        
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/add_reference")

    return redirect("/")
