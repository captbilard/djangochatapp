from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

# Create your views here.
def homepage(request):
    return render(request, "core/frontpage.html")

def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
        return render(request, 'core/sign-up.html', {'form':form})