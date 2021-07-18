from django.urls import path
from . import views

urlpatterns = [
    path('fee1/',views.fee1),
    path('fee2/',views.fee2),
]
