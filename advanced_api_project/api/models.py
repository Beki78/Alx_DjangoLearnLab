from django.db import models

#creating author model with name field
class Author(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name


#creating book model with title, publication_year and author field
class Book(models.Model):
    title = models.CharField(max_length=255)      
    publication_year = models.IntegerField() 
    # A foreign key linking to the Author model, establishing a one-to-many relationship.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  
    def __str__(self):
        return self.title
