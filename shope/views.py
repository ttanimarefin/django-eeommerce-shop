from django.shortcuts import render

def Master(request):
    return render(request, 'master.html')

def Index(request):
    return render(request,'index.html')