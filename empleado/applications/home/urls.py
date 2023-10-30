from django.urls import path
from . import views #que se importen todos los archivos

urlpatterns = [
    path('lista/', views.PruebaListView.as_view()),#as_view porque es heredado 
    path('home/', views.IndexView.as_view()),#as_view porque es heredado 
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),#as_view porque es heredado 
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),#as_view porque es heredado 
]

