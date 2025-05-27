def add_book(library, isbn, title, author, year):
    """Calcule le produit de deux nombres."""
    library[isbn] = {"title": title, "author": author, "year": year, "available": True}
    return library

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    return library

def update_author(library, isbn, new_author):
    if isbn in library:
        library[isbn]["author"] = new_author
    return library

def update_year(library, isbn, new_year):
    # Met à jour l'année
    if isbn in library:
        library[isbn]["year"] = new_year
    return library

def borrow_book(library, isbn):
    if isbn in library and library[isbn]["available"]:
        library[isbn]["available"] = False
    return library

def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
    return library

def is_book_available(library, isbn):
    return library.get(isbn, {}).get("available", False)

def get_book_info(library, isbn):
    return library.get(isbn, None)

def list_available_books(library):
    return [isbn for isbn, info in library.items() if info["available"]]

def count_books_by_author(library, author):
    return sum(1 for info in library.values() if info["author"] == author)