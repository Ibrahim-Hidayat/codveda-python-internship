from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, TaskForm
from .models import Task


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


def get_task_or_403(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user and not request.user.is_staff:
        raise PermissionDenied
    return task


@login_required
def task_list(request):
    if request.user.is_staff:
        tasks = Task.objects.select_related("owner")
    else:
        tasks = Task.objects.filter(owner=request.user)
    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        return redirect("task_list")
    return render(request, "tasks/task_form.html", {"form": form, "heading": "New Task"})


@login_required
def task_update(request, pk):
    task = get_task_or_403(request, pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("task_list")
    return render(request, "tasks/task_form.html", {"form": form, "heading": "Edit Task"})


@login_required
def task_delete(request, pk):
    task = get_task_or_403(request, pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})
