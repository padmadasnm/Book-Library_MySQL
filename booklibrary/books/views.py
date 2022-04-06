from django.shortcuts import render, redirect
from .models import MyUser, Books
from books import forms
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from books.decorators import signin_required
from django.utils.decorators import method_decorator


# Create your views here.

# ---------------- Account Creation & Login ------------------------

class RegistrationFormView(CreateView):
    model = MyUser
    template_name = "registration.html"
    form_class = forms.RegistrationForm
    success_url = reverse_lazy("login")


class LogInView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.SigninForm()
        return context

    def post(self, request, *args, **kwargs):
        form = forms.SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


def admin_logout(request):
    logout(request)
    return redirect("s_home")


#  ----------------- Admin Books -------------------------------------------

@method_decorator(signin_required, name="dispatch")
class BooksHomePage(TemplateView):
    template_name = "home.html"


@method_decorator(signin_required, name="dispatch")
class BookAddView(CreateView):
    model = Books
    template_name = "bookadd.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("home")


@method_decorator(signin_required, name="dispatch")
class ListAllBooks(ListView):
    model = Books
    template_name = "listallbooks.html"
    context_object_name = "books"


@method_decorator(signin_required, name="dispatch")
class BookEditView(UpdateView):
    model = Books
    form_class = forms.BookForm
    template_name = "editbook.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listbooks")


@method_decorator(signin_required, name="dispatch")
class BookDetailView(DetailView):
    model = Books
    template_name = "bookdetails.html"
    context_object_name = "book"
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name="dispatch")
class BookDeleteView(DeleteView):
    model = Books
    template_name = "bookdelete.html"
    context_object_name = "book"
    success_url = reverse_lazy("listbooks")
    pk_url_kwarg = 'id'


#  -------------------- Student View -------------------------------------------

class StudentHomePage(TemplateView):
    template_name = "s_home.html"


class StudentAllBooks(ListView):
    model = Books
    template_name = "s_allbooks.html"
    context_object_name = "books"


class StudentBookDetails(DetailView):
    model = Books
    template_name = "s_bookdetails.html"
    context_object_name = "book"
    pk_url_kwarg = 'id'
