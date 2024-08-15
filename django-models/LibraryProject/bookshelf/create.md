# Creating a Book Instance in Django Shell

## Python Command

```python
from myapp.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
