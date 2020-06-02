from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add),
    path('seeRun/', views.seeRun),
    path('seeDone/', views.seeDone),
    
]
