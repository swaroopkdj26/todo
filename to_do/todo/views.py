from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todo


def index(request):
    all_todo=todo.objects.all()
    return  render(request,'home.html',
    {"all_items":all_todo})

def Add_todo(request):
    new_item = todo(content =request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deletetodo(request,todo_id):
    item_to_delete=todo.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')