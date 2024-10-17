from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.veiwfeedback,name="veiwfeedback"),
  path('writefeedback/',views.writefeedback,name="writefeedback"),
  path("succesfully/",views.succesfully,name="sucessfully"),
   
   
]
