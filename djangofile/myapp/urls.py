from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('form/', views.index, name='index'),
    path('letter/', views.letter, name='letter'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),

]