from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .models import Library
from .models import Book
from .models import UserProfile 

# Book listing view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Library detail view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Custom logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# User registration view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST.get('role', 'Member')  # Default role is 'Member'
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, role=role)  # Create UserProfile with role
        login(request, user)
        return redirect('list_books')
    return render(request, 'relationship_app/register.html')

# Role-Based Access Control Views

# Admin view (restricted to 'Admin' role)
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view (restricted to 'Librarian' role)
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view (restricted to 'Member' role)
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
