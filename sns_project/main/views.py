from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/show_main.html')

def showinfo(request):
    return render(request, 'main/show_info.html')

def mainpage(request):
    return render(request, 'main/mainpage.html')