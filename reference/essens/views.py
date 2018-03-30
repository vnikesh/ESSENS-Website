from django.shortcuts import render

# Create your views here.

#from django.utils import timezone
#from .models import *
from django.shortcuts import render, get_object_or_404
#from django.shortcuts import redirect
#from django.contrib.auth.decorators import login_required
#from .forms import *
#from django.db.models import Sum



def home(request):
    return render(request, 'essens/home.html',
                 {'essens': home})

def reference(request):
    return render(request, 'essens/reference.html',
                  {'essens': reference})

def core(request):
    return render(request, 'essens/core.html',
                  {'essens': core})

def basicio(request):
    return render(request, 'essens/basicio.html',
                  {'essens': basicio})

def basicsetops(request):
    return render(request, 'essens/basicsetops.html',
                  {'essens': basicsetops})

def basictraversal(request):
    return render(request, 'essens/basictraversal.html',
                  {'essens': basictraversal})

def basicchange(request):
    return render(request, 'essens/basicchange.html',
                  {'essens': basicchange})

def basicanalysis(request):
    return render(request, 'essens/basicanalysis.html',
                  {'essens': basicanalysis})


# Create your views here.
