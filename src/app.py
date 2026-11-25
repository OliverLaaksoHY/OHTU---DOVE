"""Flask routes for managing book references."""

from flask import flash, jsonify, redirect, render_template, request

import utils
from config import app, test_env
from db_helper import reset_db
from repositories.book_reference_repository import (
    db_create_reference,
    db_update_book_reference,
    get_reference_by_id,
    get_references,
    db_delete_reference
)

@app.route("/")
def index():
    """Render the home page with all saved references."""
    references = get_references()
    return render_template("index.html", references=references)

@app.route("/add_reference")
def add_reference():
    """Render the form for adding a reference."""
    return render_template("add_reference.html")

@app.route("/create_reference", methods=["POST"])
def create_reference():
    """Validate and save a submitted reference."""
    title = request.form["title"].strip()
    author = request.form["author"].strip()
    year = request.form["year"]

    try:
        utils.validate_text_entries([("title", title), ("author", author)])
        utils.validate_year_entry(year)
        db_create_reference(title, author, year)
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(str(error))
        return redirect("/add_reference")

    return redirect("/")

@app.route("/reference/<int:reference_id>")
def show_reference(reference_id):
    """Render the detail page for one reference."""
    reference = get_reference_by_id(reference_id)
    if not reference:
        return "Reference not found", 404
    return render_template("show_reference.html", reference=reference)

# EDIT REFERENCE BEGING
@app.route("/edit_reference/<int:reference_id>")
def edit_reference(reference_id):
    """Render the edit form for one reference."""
    reference = get_reference_by_id(reference_id)
    if not reference:
        return "Reference not found", 404
    return render_template("edit_reference.html", reference=reference)

@app.route("/update_reference", methods=["POST"])
def update_reference():
    """Validate and update a submitted reference."""
    title = request.form["title"].strip()
    author = request.form["author"].strip()
    year = request.form["year"]
    reference_id = request.form["reference_id"]

    try:
        utils.validate_text_entries([("title", title), ("author", author)])
        utils.validate_year_entry(year)
        db_update_book_reference(reference_id, title, author, year)
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(str(error))
        return redirect("/edit_reference/" + reference_id)

    return redirect("/")
# EDIT REFERENCE END

@app.route("/delete_reference/<int:reference_id>", methods=["GET", "POST"])
def delete_reference(reference_id):
    """Render the delete confirmation page or delete a reference."""
    reference = get_reference_by_id(reference_id)
    if not reference:
        return "Reference not found", 404

    if request.method == "GET":
        return render_template("delete_reference.html", reference=reference)
    if request.method == "POST":

        if "delete" in request.form:
            db_delete_reference(reference_id)
            return redirect("/")
        else:
            return redirect("/reference/" + str(reference_id))

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        """Clear reference data for tests."""
        reset_db()
        return jsonify({"message": "db reset"})
