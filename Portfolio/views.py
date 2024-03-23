from django.shortcuts import render
from al_content.models import Category, Projects
def home(request):
    return render(request,'home.html')
def home(request, category_slug = None):
    data = Projects.objects.all()
    if category_slug is not None:
        category = Category.objects.get(name = category_slug)
        data = Projects.objects.filter(catagory=category)
    categories = Category.objects.all()
    return render(request, 'home.html',{'data': data, 'category': categories,})