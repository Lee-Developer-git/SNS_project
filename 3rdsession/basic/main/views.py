from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def first(request):
    return render(request, 'main/first.html')

def second(request):
    return render(request, 'main/second.html')