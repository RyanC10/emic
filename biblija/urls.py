from django.urls import path
from biblija.views import pocetna,majaforma
from . import views

urlpatterns = [

    path('pocetna', pocetna.as_view()),
    path('netocno', views.netocno, name='netocno'),
   
    path('e02/',views.e02),
    path('kraj/<radnom>/',views.kraj),
    path(r'download/', views.ispis, name='ispis'),
    
      path('maja', views.maja, name='maja'),

    path('majaforma', majaforma.as_view()),
     path('downloadmaja/', views.ispismaja, name='ispis'),
    
   
   
]   
