from django.urls import path
from .import views 
urlpatterns = [
     path ('Home/',views.func,name="func"),
   
]
