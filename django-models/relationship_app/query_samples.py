from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    # Retrieve the author instance using the author's name
    author = Author.objects.get(name=author_name)
    # Filter books by the retrieved author instance
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def query_books_in_library(library_name):
    # Retrieve the library instance using the library's name
    library = Library.objects.get(name=library_name)
    # Get all books related to the library
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    # Retrieve the library instance using the library's name
    library = Library.objects.get(name=library_name)
    # Get the librarian associated with the library
    librarian = library.librarian
    return librarian

# Sample Usage
if __name__ == "__main__":
    # Query all books by a specific author
    author_books = query_books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:")
    for book in author_books:
        print(book.title)

    # List all books in a library
    library_books = query_books_in_library("Central Library")
    print("\nBooks in Central Library:")
    for book in library_books:
        print(book.title)

    # Retrieve the librarian for a library
    librarian = query_librarian_for_library("Central Library")
    print(f"\nLibrarian for Central Library: {librarian.name}")
