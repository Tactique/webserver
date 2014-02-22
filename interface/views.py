from django.shortcuts import render
from django.template import Context, RequestContext

# Create your views here.
def index(request):
    c = RequestContext(request, {})
    return render(request, 'interface/index.html', c)