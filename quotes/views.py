from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .utilite import get_mongodb
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote
from bson import ObjectId
from django.contrib.auth.decorators import login_required


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def authors(request):
    db = get_mongodb()
    authors = db.authors.find()
    return render(request, "quotes/authors.html", context={"authors": authors})


def author_description(request, author_name):
    author_name = author_name.replace("-", " ")
    db = get_mongodb()
    authors = db.authors.find()
    for author in authors:
        if author["fullname"] == author_name:
            return render(
                request,
                "quotes/author_description.html",
                context={
                    "name": author["fullname"],
                    "born_date": author["born_date"],
                    "born_location": author["born_location"],
                    "description": author["description"],
                },
            )


@login_required()
def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == "POST":
        db = get_mongodb()
        db.authors.insert_one(
            {
                "fullname": request.POST.get("fullname"),
                "born_date": request.POST.get("born_date"),
                "born_location": request.POST.get("born_location"),
                "description": request.POST.get("description"),
            }
        )

        return redirect(to="quotes:authors")

    return render(request, "quotes/add_author.html", context={"form": form})


@login_required()
def add_quotes(request):
    form = QuoteForm(instance=Quote())
    if request.method == "POST":
        db = get_mongodb()
        author = db.authors.find_one({"fullname": request.POST.get("author")})
        if author:
            db.quotes.insert_one(
                {
                    "quote": request.POST.get("quote"),
                    "tags": request.POST.get("tags").split(","),
                    "author": ObjectId(author["_id"]),
                }
            )
        print(request.POST.get("tags"))
        return redirect(to="/")

    return render(request, "quotes/add_quote.html", context={"form": form})
