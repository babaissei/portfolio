from django.shortcuts import render

def index(request):
    return render(request, 'profileapp/index.html')

def profile(request):
    return render(request, 'profileapp/profile.html')

def test(request):
    return render(request, 'profileapp/test.html')
