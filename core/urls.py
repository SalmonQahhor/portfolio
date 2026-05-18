from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/submit/', views.contact_submit, name='contact_submit'), # Yangi yo'l
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('links/', views.links, name='links'),
]