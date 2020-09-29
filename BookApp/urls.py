from django.urls import path
from .views import BookView, CreateBookView, DetailBookView, DeleteBookView

urlpatterns = [
    path('', BookView.as_view(), name="book"),
    path('create-book/', CreateBookView.as_view(), name="create-book"),
    path('detail-book/<slug:slug>', DetailBookView.as_view(), name="detail"),
    path('delete-book/<int:id>', DeleteBookView.as_view(), name="delete-book"),
]