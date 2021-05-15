from django.urls import path
from . import views

app_name= 'djangostudy'
urlpatterns = [
    # viewsからindexを読み込んで、nameをindexに
    path('', views.index, name='index'),
    path('works', views.works, name='works'),
]