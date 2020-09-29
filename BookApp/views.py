from django import forms
from django.shortcuts import render, redirect
from django.views import View

from BookApp.models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ["title", "media", "price", "body"]

        widgets = {
            "title": forms.TextInput(attrs=({
                "class": "form-control",
                "placeholder": "Title text goes here..."
            })),
            "body": forms.Textarea(attrs=({
                "class": "form-control",
                "placeholder": "Title text goes here..."
            })),
            "price": forms.NumberInput(attrs=({
                "class": "form-control",
                "placeholder": "Title text goes here..."
            })),
        }


class BookView(View):

    def get(self, request):
        template_name = "book.html"
        books = BookModel.objects.all()
        context = {"books": books}
        return render(request, template_name, context)


class DetailBookView(View):
    template_name = "detail-book.html"

    def get(self, request, *args, **kwargs):
        _slug = self.kwargs.get("slug")
        queryset = BookModel.objects.get(slug=_slug)
        context = {"object": queryset}
        return render(request, self.template_name, context)


class CreateBookView(View):
    form = BookForm()
    template_name = "create-book.html"
    context = {"form": form}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, self.context)


class UpdateBookView(View):
    form = BookForm()
    template_name = "update-book.html"
    context = {"form": form}
    def get(self, request, *args, **kwargs):
        _id = self.kwargs.get("id")
        queryset = BookModel.objects.get(id=_id)
        # context = {"form": queryset}
        return render(request, self.template_name, self.context)

class DeleteBookView(View):
    def get(self, request, *args, **kwargs):
        _id = self.kwargs.get("id")
        BookModel.objects.filter(id=_id).delete()
        return redirect("book")
