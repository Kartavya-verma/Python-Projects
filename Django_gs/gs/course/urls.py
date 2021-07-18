from django.urls import path
from . import views

urlpatterns = [
    path('cour1/',views.course1),
    path('cour2/',views.course2),
]
