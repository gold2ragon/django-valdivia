from django.shortcuts import render
from django.http import HttpResponse
# from django.utils.translation import gettext as _
from django.utils import translation
from projects.models import Category, Project

# Create your views here.
def home(request):

    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def bio(request):
    return render(request, 'bio.html', {'menu': 0})

def jobs(request):
    categories = Project.objects.filter(is_principal=True).order_by('category')
    return render(request, 'jobs.html', {'menu': 1, 'categories': categories})

def contact(request):
    return render(request, 'contact.html', {'menu': 2})

def category(request, index):
    categories = Category.objects.all()
    projects = Project.objects.filter(category=categories[index])
    return render(request, 'category4.html', {'menu': 1, 'index': index, 'projects': projects})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project.html', {'menu': 1, 'project': project})

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'allprojects.html', {'menu': 1, 'projects': projects})