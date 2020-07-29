from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import todoList
from .forms import TodoListForm


def home(request):

    todoListItemsAll = todoList.objects.all()
    todoListItems = todoListItemsAll.filter(completed=False).order_by('-created_on')
    completedItem = todoListItemsAll.filter(completed=True).order_by('-created_on')
  
    # create new task

    form = TodoListForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = TodoListForm()
    else:
        form = TodoListForm()

    return HttpResponse(render(request,'todo/index.html',context={'todoListItems':todoListItems,'completedItem':completedItem,'form':form}))

# update task 

def update(request,id):
    
    instance = get_object_or_404(todoList,id=id)

    form = TodoListForm(request.POST or None,instance=instance)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'todo/update.html',context= {'form': form})


def delete(request,id):
    
    instance = get_object_or_404(todoList,id=id)

    if request.method == 'POST':
        instance.delete()
        return redirect('/')
    return render(request,'todo/delete.html')


def complete(request,id):
     instance = todoList.objects.filter(id=id).update(completed=True)
     return redirect('/')


def deleteAll(request):
    instance = todoList.objects.filter(completed=True)
    if instance:
        instance.delete()
        return redirect('/')
    
def about(request):
    return HttpResponse(render(request,'todo/about.html'))