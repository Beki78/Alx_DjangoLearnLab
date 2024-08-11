from bookshelf.models import Book
# Delete the book instance
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
