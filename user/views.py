from django.shortcuts import render

def archivo(request):
    return render(request, 'user/archivo.html', {})