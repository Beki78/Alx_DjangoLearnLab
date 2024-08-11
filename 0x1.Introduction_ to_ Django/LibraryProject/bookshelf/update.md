book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")