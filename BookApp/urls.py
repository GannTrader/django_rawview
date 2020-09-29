from django.urls import path
from .views import BookView, CreateBookView, DetailBookView, DeleteBookView, UpdateBookView

urlpatterns = [
    path('', BookView.as_view(), name="book"),
    path('create-book/', CreateBookView.as_view(), name="create-book"),
    path('update-book/<int:id>', UpdateBookView.as_view(), name="update-book"),
    path('detail-book/<slug:slug>', DetailBookView.as_view(), name="detail"),
    path('delete-book/<int:id>', DeleteBookView.as_view(), name="delete-book"),
]