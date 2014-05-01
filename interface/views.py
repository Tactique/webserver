from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.template import RequestContext

# Create your views here.
def login(request):
    has_next = 'next' in request.GET
    if request.user.is_authenticated():
        if has_next:
            return redirect(request.GET['next'])
        else:
            return redirect('/play/')
    else:
        forms = {
            'login_form': AuthenticationForm(),
            'registration_form': UserCreationForm(),
        }
        return render(request, "interface/login.html", forms)

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
