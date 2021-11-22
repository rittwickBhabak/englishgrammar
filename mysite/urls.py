from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('learn/', include('learn.urls')),
    path('practice/', include('practice.urls')),
]