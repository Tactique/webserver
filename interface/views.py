from django.shortcuts import render
from django.template import Context, RequestContext

# Create your views here.
def login(request):
    c = RequestContext(request, {})
    return render(request, 'interface/login.html', c)

def index(request):
    c = RequestContext(request, {})
    return render(request, 'interface/index.html', c)

def tests(request):
    c = RequestContext(request, {})
    return render(request, 'interface/tests.html', c)

def editor(request):
    c = RequestContext(request, {})
    return render(request, 'interface/editor.html', c)