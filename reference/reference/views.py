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



# Create your views here.
