from django.contrib import admin
from django.urls import path, include
from landing import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]