from django.urls import path
from introduce import views

urlpatterns = [
    path('', views.index, name = 'index'),
]