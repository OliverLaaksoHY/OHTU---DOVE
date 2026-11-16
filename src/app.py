from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env
import utils

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
    except Exception as error:
        flash(str(error))
        return redirect("/add_reference")

    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
