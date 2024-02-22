from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
# Create your views here.

def front_page(request):
    return render(request, 'ChatCommunicationApp/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('frontpage')
        else:
            print(form.errors)
    else:

        form = SignUpForm()
    return render(request, 'ChatCommunicationApp/signup.html', {'form': form})