from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("<slug:slug>",views.book_detial,name="book-detail")
]
