from django.urls import path
from . import views


urlpatterns = [
   path('',views.home, name='home'),
   path('about/', views.about, name='about'), 
   path('contact/', views.contact, name='contact'),
   path('admin_page/', views.admin_page, name='admin_page'),
   path('signout/', views.signout, name="signout"),
   path('add_doctor/', views.add_doctor, name="add_doctor"),
   path('view_doctors/', views.view_doctors, name='view_doctors'),

]