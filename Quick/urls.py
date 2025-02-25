from django.contrib import admin
from django.urls import path
from Quick import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('gallery/', views.gallery,name='gallery'),
    path('About/', views.About,name='About'),
    path('form/', views.form,name='form'),
    path('product/', views.product,name='product'),
    path('services/', views.services,name='services'),

]
