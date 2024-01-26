from django.urls import path
from . import views


urlpatterns=[
    path('book-list/',views.ShowAllBooks,name='Retrieving all the books'),
    path('book-detail/<int:pk>',views.ViewParticularBook,name='Retrive the particular book'),
    path('book-create/',views.AddTheBook,name='Add the book'),
    path('book-update/<int:pk>',views.UpdateTheBookDetails,name='Update the Book'),
    path('book-delete/<int:pk>',views.DeleteTheBook,name='Delete the Book'),
]