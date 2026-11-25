"""Database operations for book references."""

from sqlalchemy import text

from config import db
from entities.book_reference import Reference


def get_references():
    """Return all references as domain entities."""
    result = db.session.execute(text("SELECT id, title, author, year FROM book_references"))
    references = result.fetchall()
    return [Reference(ref[0], ref[1], ref[2], ref[3]) for ref in references]


def db_create_reference(title, author, year):
    """Insert a reference and commit the transaction."""
    sql = text("INSERT INTO book_references (title, author, year) VALUES (:title, :author, :year)")
    db.session.execute(sql, { "title": title, "author": author, "year": year })
    db.session.commit()


def db_update_book_reference(reference_id, title, author, year):
    """Update a reference and commit the transaction."""
    sql = text(
        "UPDATE book_references SET title = :title, author = :author, "
        "year = :year WHERE id = :id"
    )
    db.session.execute(sql, { "title": title, "author": author, "year": year, "id": reference_id })
    db.session.commit()


def get_reference_by_id(reference_id):
    """Return one reference by ID, or None if it does not exist."""
    sql = text("SELECT id, title, author, year FROM book_references WHERE id = :id")
    result = db.session.execute(sql, { "id": reference_id })
    reference = result.fetchone()
    if reference:
        return Reference(reference[0], reference[1], reference[2], reference[3])
    return None

def db_delete_reference(reference_id):
    """Delete a reference and commit the transaction."""
    sql = text("DELETE FROM book_references WHERE id = :id")
    db.session.execute(sql, { "id": reference_id })
    db.session.commit()
