from django.http import request
from django.shortcuts import render,redirect
from .models import Public
from django.views.generic import ListView, DetailView, CreateView,DeleteView, UpdateView
from .forms import PublicForm
from django.urls import reverse_lazy

class Getlist(ListView):
    model = Public
    template_name = 'news/news.html'  

class Getdetail(DetailView):
    model = Public
    template_name = 'news/detail.html'   

class Getdelete(DeleteView):
    model = Public
    success_url = '/news/'
    template_name = 'news/news_delete.html'
     
class Getupdate(UpdateView):
    model = Public
    form_class = PublicForm  
    template_name = 'news/create.html'
      

def create(request):
    error = ''
    if request.method == 'POST':
        form = PublicForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            error = 'Form is not valid !'

    form = PublicForm()
    data = {'forma': form }
    return render(request, 'news/create.html', data)   

def update(request):
    error = ''
    if request.method == 'POST':
        form = PublicForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Form is not valid !'

    form = PublicForm()
    data = {'forma': form }
    return render(request, 'news/update.html', data)  