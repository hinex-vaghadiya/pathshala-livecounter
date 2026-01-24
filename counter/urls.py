from django.urls import path
from . import views

urlpatterns = [
    path("", views.button_page),
    path("counter/", views.counter_page),
    path("increment/", views.increment_counter),
    path("count/", views.get_counter),
]
