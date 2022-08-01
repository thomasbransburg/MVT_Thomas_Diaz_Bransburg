from django.http import HttpResponse
from django.template import Template, Context, loader

def hello(request):
    return HttpResponse("tengo vida")

