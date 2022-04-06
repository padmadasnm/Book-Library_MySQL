from django.urls import path
from books import views

urlpatterns = [
    path("accounts/registration", views.RegistrationFormView.as_view(), name="signup"),
    path("accounts/login", views.LogInView.as_view(), name="login"),
    path("accounts/logout", views.admin_logout, name="logout"),
    path("book/home", views.BooksHomePage.as_view(), name="home"),
    path("book/add", views.BookAddView.as_view(), name="bookadd"),
    path("book/listbooks", views.ListAllBooks.as_view(), name="listbooks"),
    path("book/listbooks/editbook/<int:id>", views.BookEditView.as_view(), name="editbook"),
    path("book/listbooks/bookdetails/<int:id>", views.BookDetailView.as_view(), name="bookdetails"),
    path("book/listbooks/removebook/<int:id>", views.BookDeleteView.as_view(), name="removebook"),
    path("", views.StudentHomePage.as_view(), name="s_home"),
    path("student/allbooks",views.StudentAllBooks.as_view(),name="allbooks"),
    path("student/allbooks/s_bookdetails/<int:id>",views.StudentBookDetails.as_view(),name="s_bookdetails"),
]
