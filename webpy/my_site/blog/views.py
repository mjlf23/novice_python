from django.shortcuts import render

from django.http import HttpResponse

from blog import models

# Create your views here.

def hello(request):
    return HttpResponse("欢迎使用Django!")

def index(request):
    blog_index = models.Article.objects.all().order_by("-id")
    context = {"blog_index":blog_index,}
    return render(request, "index.html", context)

def page_not_found(request, exception):
    return render(request, "404.html")
def page_error(request):
    return render(request, "500.html")
def permission_denied(requestk, exception):
    return render(request, "403.html")
def bad_request(request, exception):
    return render(request, "400.html")