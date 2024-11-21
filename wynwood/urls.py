from django.contrib import admin
from django.urls import path
from landing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change_i18n/', views.change_i18n, name='change_i18n'),
    path('admin/', admin.site.urls),
]