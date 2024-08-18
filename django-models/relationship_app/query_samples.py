from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

if __name__ == "__main__":
    author_books = query_books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:")
    for book in author_books:
        print(book.title)

    library_books = query_books_in_library("Central Library")
    print("\nBooks in Central Library:")
    for book in library_books:
        print(book.title)

    librarian = query_librarian_for_library("Central Library")
    print(f"\nLibrarian for Central Library: {librarian.name}")
