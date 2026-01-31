# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Counter


def button_page(request):
    return render(request, "button.html")


def counter_page(request):
    return render(request, "counter.html")


def update_counter(request, branch, action):
    counter, _ = Counter.objects.get_or_create(branch=branch)

    if action == "inc":
        counter.value += 1
    elif action == "dec" and counter.value > 0:
        counter.value -= 1

    counter.save()
    return JsonResponse({"branch": branch, "value": counter.value})


def get_counters(request):
    data = {
        c.branch: c.value for c in Counter.objects.all()
    }
    return JsonResponse(data)
