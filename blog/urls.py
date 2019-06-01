from django.urls import path
from . import views

urlpatterns = [
    path('html/', views.html, name='html'),
    path('md/', views.md_to_html, name='md_to_html')
]
