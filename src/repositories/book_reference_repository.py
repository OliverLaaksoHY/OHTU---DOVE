from config import db
from sqlalchemy import text
from entities.book_reference import Reference

def get_references():
    result = db.session.execute(text("SELECT id, title, author, year FROM book_references"))
    references = result.fetchall()
    return [Reference(ref[0], ref[1], ref[2], ref[3]) for ref in references]

def db_create_reference(title, author, year):
    sql = text("INSERT INTO book_references (title, author, year) VALUES (:title, :author, :year)")
    db.session.execute(sql, { "title": title, "author": author, "year": year })
    db.session.commit()

def get_reference_by_id(reference_id):
    sql = text("SELECT id, title, author, year FROM book_references WHERE id = :id")
    result = db.session.execute(sql, { "id": reference_id })
    reference = result.fetchone()
    if reference:
        return Reference(reference[0], reference[1], reference[2], reference[3])
    return None