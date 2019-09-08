from django.http import HttpResponse

def index(request):
    return HttpResponse("hello django")

def about(request):
    return HttpResponse("about")
def f():
    pass