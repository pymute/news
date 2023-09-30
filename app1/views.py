from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {
        'title': 'Home Page',
        'heading': 'Welcome to Home page!',
        'content': 'This is some content for Home page.',
    }
    return render(request, 'index.html', context)


def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def about(request):
    my_list = ['item1', 'item2', 'item3']
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    welcome_text = True
    context = {
        'list': my_list,
        'dict': my_dict,
        'welcome_text': welcome_text
    }
    return render(request, 'index2.html', context)