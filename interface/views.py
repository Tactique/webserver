from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template import Context, RequestContext

# Create your views here.
def login(request):
    has_next = 'next' in request.GET
    if request.user.is_authenticated():
        if has_next:
            return redirect(request.GET['next'])
        else:
            return redirect('/play/')
    else:
        c = RequestContext(request, {})
        return render(request, "interface/login.html", c)

@login_required
def index(request):
    c = RequestContext(request, {})
    return render(request, 'interface/index.html', c)

def tests(request):
    c = RequestContext(request, {})
    return render(request, 'interface/tests.html', c)

def editor(request):
    c = RequestContext(request, {})
    return render(request, 'interface/editor.html', c)