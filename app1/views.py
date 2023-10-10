from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Project
from .form import ProjectForm

def pro_list(request):
    pro = Project.objects.all()
    return render(request, 'my_temp/read.html', {'pro': pro})

def pro_detail(request, pk):
    pro = get_object_or_404(Project, pk=pk)
    return render(request, 'templates/read.html', {'pro': pro})


def pro_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.save()
            return redirect('pro_detail', pk=pro.pk)
    else:
        form = ProjectForm()
    return render(request, 'templates/update.html', {'form': form})


def pro_edit(request, pk):
    pro = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=pro)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.save()
            return redirect('book_detail', pk=pro.pk)
    else:
        form = ProjectForm(instance=pro)
    return render(request, 'templates/create.html', {'form': form})


def pro_delete(request, pk):
    pro = get_object_or_404(Project, pk=pk)
    pro.delete()
    return redirect('pro_list')

