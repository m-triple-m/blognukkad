from django.shortcuts import render

def Login(request):
    if request.method == 'POST':
        form = Auth
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')