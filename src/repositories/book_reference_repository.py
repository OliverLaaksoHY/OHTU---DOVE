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
