from django.shortcuts import render

def showtree(request):
    return render(request, 'showtree/index.html')