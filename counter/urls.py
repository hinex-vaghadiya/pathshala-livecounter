# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.button_page),
    path("counter/", views.counter_page),

    path("update/<str:branch>/<str:action>/", views.update_counter),
    path("counts/", views.get_counters),
]
