"""Convert book references into BibTeX entries."""

import re

_BIBTEX_SPECIAL_CHARACTERS = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
    "\\": r"\textbackslash{}",
}


def remove_bibtex(value):
    """Remove characters that have BibiTex meaning."""
    clean_string = ""
    for char in str(value):
        clean_string = clean_string + _BIBTEX_SPECIAL_CHARACTERS.get(char, char)
    return clean_string


def citation_key(reference):
    """Build a citation key from the author surname and year."""
    author = reference.author.strip()


    words = author.split()
    surname = words[-1]
    if "," in author:
        surname = author.split(",")[0]

    # removes all things that match \W+ which limits the string to only numbers
    surname = re.sub(r"\W+", "", surname).lower() or "reference"

    return f"{surname}{reference.year}"


def to_bibtex(reference):
    """Format a reference as a BibTeX @book entry."""
    return (
        f"@book{{{citation_key(reference)},\n"
        f"  title = {{{remove_bibtex(reference.title)}}},\n"
        f"  author = {{{remove_bibtex(reference.author)}}},\n"
        f"  year = {{{reference.year}}}\n"
        "}\n"
    )
