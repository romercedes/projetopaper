from django.urls import include, path
from django.contrib import admin

from . import views

app_name='questoes'
urlpatterns = [
   path('', views.index, name='index'),
    path('lista', views.lista, name='lista'),
    path('<int:question_id>/', views.detail, name='detail'),  
    path('<int:question_id>/resultados/', views.resultados, name='resultados'), 
    path('<int:question_id>/resposta/', views.resposta, name='resposta'),

    # local
    path('', include('pages.urls', namespace='pages')),
]