from django.shortcuts import render
from django.http import JsonResponse
from .models import Counter

# Create your views here.


def button_page(request):
    return render(request, "button.html")

def counter_page(request):
    return render(request, "counter.html")

def increment_counter(request):
    counter = Counter.objects.first()
    counter.value += 1
    counter.save()
    return JsonResponse({"value": counter.value})

def get_counter(request):
    counter = Counter.objects.first()
    return JsonResponse({"value": counter.value})
