from django.shortcuts import render
from django.http import JsonResponse
from .models import Counter

# Create your views here.


def button_page(request):
    return render(request, "button.html")

def counter_page(request):
    return render(request, "counter.html")

def increment_counter(request):
    counter, created = Counter.objects.get_or_create(id=1, defaults={"value": 0})
    counter.value += 1
    counter.save()
    return JsonResponse({"value": counter.value})

def get_counter(request):
    counter, created = Counter.objects.get_or_create(id=1, defaults={"value": 0})
    return JsonResponse({"value": counter.value})
