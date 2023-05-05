
from django.contrib import admin
from django.urls import path

import App.views
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('characters/<int:character_id>/', views.detail_view, name='detail_view'),
    path('episodes/', views.episode_list, name='episode_list'),
    path('episodes/<int:episode_id>/', views.episode_detail, name='episode_detail')
]
