
from django.contrib import admin
from django.urls import path

import App.views
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('detail/<int:character_id>/', views.detail_view, name='detail'),
]
