from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import Todolist
from django.urls import reverse
# Create your views here.

def index(request):
    _todo = Todolist.objects.all()
    return render(request, 'index.html', {'todo' : _todo})

# 리스트에 할 일 추가
def create(request):
    content = request.POST['todoContent']
    todo_new = Todolist(title=content)
    todo_new.save()
    return HttpResponseRedirect(reverse('index'))

# 리스트에서 일정 삭제
def delete(request):
    _id = request.GET['todoNum']
    todo = Todolist.objects.get(id=_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))