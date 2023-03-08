from django.urls import path
from biblija.views import pocetna
from . import views

urlpatterns = [

    path('pocetna', pocetna.as_view()),
    path('netocno', views.netocno, name='netocno'),
   
    path('e02/',views.e02),
    path('kraj/<radnom>/',views.kraj),
    
   
   
]   