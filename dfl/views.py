from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about-us.html")

def contact(request):
    return render(request, "contact.html")

def main(request):
    return render(request, "main.html")

def news(request):
    return render(request, "news.html")

def search(request):
    return render(request, "search-result.html")

def single(request):
    return render(request, "single-property.html")