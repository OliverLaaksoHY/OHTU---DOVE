"""Database setup and test reset helpers."""

import os

from sqlalchemy import text

from config import app, db


def reset_db():
    """Clear all entries from the book_references table."""
    print("Clearing contents from table book_references")
    sql = text("DELETE FROM book_references")
    db.session.execute(sql)
    db.session.commit()


def tables():
    """Return all table names from the database."""
    sql = text(
        "SELECT name FROM sqlite_master "
        "WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]


def setup_db():
    """Create the database schema, dropping existing tables first."""
    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table}")
            db.session.execute(sql)
        db.session.commit()

    print("Creating database")

    # Read schema from schema.sql file
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as schema_file:
        schema_sql = schema_file.read().strip()

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
