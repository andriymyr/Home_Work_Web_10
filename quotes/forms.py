from django.forms import ModelForm, TextInput, ImageField, FileInput, CharField
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(
        max_length=150, widget=TextInput(attrs={"class": "form-control"})
    )
    born_date = CharField(
        max_length=150, widget=TextInput(attrs={"class": "form-control"})
    )
    born_location = CharField(
        max_length=150, widget=TextInput(attrs={"class": "form-control"})
    )
    description = CharField(
        max_length=150, widget=TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(ModelForm):
    quote = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    tags = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    author = CharField(
        max_length=150, widget=TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Quote
        fields = ["quote", "tags", "author"]
