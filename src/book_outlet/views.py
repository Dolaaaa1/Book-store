from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from django.db.models import Avg 
#reate your views here.


def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    average_rating = books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{
      "books":books,
      "total_number_of_books":num_books,
      "average_rating": average_rating
    })





def book_detial(request, slug):
    #try:
    # book = Book.objects.get(pk=id)
    #except :
        #raise Http404()
    book = get_object_or_404(Book,slug=slug)    
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "auther":book.auther,
        "rating":book.rating,
        "is_bestseller":book.is_bestselling
     })