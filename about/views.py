from django.shortcuts import render, redirect

def about_view(request):
    return render(request, 'core/about.html')