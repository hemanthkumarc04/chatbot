from django.urls import path
from . import views 

urlpatterns = [
    # Shows the HTML webpage
    path('', views.home, name="home"), 
    
    # Processes the JSON text from the frontend
    path('api/ask-ai/', views.ask_ai, name="ask_ai"), 
]