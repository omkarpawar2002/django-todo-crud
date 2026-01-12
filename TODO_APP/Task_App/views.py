from django.shortcuts import render,redirect
from .forms import TaskForm
from django.http import HttpResponse
from .models import Task

# Create your views here.
def add_task(request):
    form = TaskForm()
    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('display_task')
        return HttpResponse("Error Occurs While Creating task")
    template_name = 'Task_App/Add_Task.html'
    context = {'form':form}
    return render(request,template_name,context)

def display_task(request):
    objs = Task.objects.all()
    template_name = 'Task_App/Display_Task.html'
    context = {'records':objs}
    return render(request,template_name,context)

def update_task(request,pk):
    obj = Task.objects.get(id=pk)
    form = TaskForm(instance=obj)
    if(request.method == 'POST'):
        form = TaskForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('display_task')
        return HttpResponse("Error Occur While Updating Task")
    template_name = 'Task_App/Update_Task.html'
    context = {'form':form}
    return render(request,template_name,context)

def delete_task(request,pk):
    obj = Task.objects.get(id=pk)
    if(request.method == 'POST'):
        obj.delete()
        return redirect('display_task')
    template_name = 'Task_App/Delete_Task.html'
    context = {'obj':obj}
    return render(request,template_name,context)