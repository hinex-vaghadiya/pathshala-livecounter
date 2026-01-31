# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Counter

# ==========================
# Pages
# ==========================
def button_page(request):
    return render(request, "button.html")

def counter_page(request):
    return render(request, "counter.html")


# ==========================
# Update counter per branch
# ==========================
def update_counter(request, branch, action):
    # Get or create counter for the given branch
    counter, _ = Counter.objects.get_or_create(branch=branch, defaults={"value": 0})

    if action == "inc":
        counter.value += 1
    elif action == "dec" and counter.value > 0:
        counter.value -= 1

    counter.save()
    return JsonResponse({"branch": branch, "value": counter.value})


# ==========================
# Return all branch counters
# ==========================
def get_counters(request):
    """
    Returns all branch counters in JSON like:
    {
        "mota_varachha": 5,
        "hirabaug": 3,
        "abrama": 2
    }
    """
    # Ensure all branches exist
    branches = ["mota_varachha", "hirabaug", "abrama"]
    for b in branches:
        Counter.objects.get_or_create(branch=b, defaults={"value": 0})

    # Collect current values
    data = {c.branch: c.value for c in Counter.objects.all()}

    return JsonResponse(data)
