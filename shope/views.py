from django.shortcuts import render
from app.models import Category,Product, Sub_Category

from app.models import Category

def Master(request):
    return render(request, 'master.html')

def Index(request):
    category=Category.objects.all()
    
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.objects.filter(Sub_category=categoryID).order_by('-id')
    else:
        product=Product.objects.all()

    context={
        'category':category,
        'product':product,
        
    }
    return render(request,'index.html',context)