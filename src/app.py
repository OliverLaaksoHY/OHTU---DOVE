from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env
import utils
from repositories.book_reference_repository import db_update_book_reference, db_create_reference, get_references, get_reference_by_id

@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)

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
        db_create_reference(title, author, year)
    except Exception as error:
        flash(str(error))
        return redirect("/add_reference")

    return redirect("/")

@app.route("/reference/<int:reference_id>")
def show_reference(reference_id):
    reference = get_reference_by_id(reference_id)
    if not reference:
        return "Reference not found", 404
    return render_template("show_reference.html", reference=reference)

# EDIT REFERENCE BEGING
@app.route("/edit_reference/<int:reference_id>")
def edit_reference(reference_id):
    reference = get_reference_by_id(reference_id)
    if not reference:
        return "Reference not found", 404
    return render_template("edit_reference.html", reference=reference)

@app.route("/update_reference", methods=["POST"])
def update_reference():
    title = request.form["title"].strip()
    author = request.form["author"].strip()
    year = request.form["year"]
    reference_id = request.form["reference_id"]

    try:
        utils.validate_text_entries([("title", title), ("author", author)])
        utils.validate_year_entry(year)
        db_update_book_reference(reference_id, title, author, year)
    except Exception as error:
        flash(str(error))
        return redirect("/edit_reference/" + reference_id)

    return redirect("/")
# EDIT REFERENCE END

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
