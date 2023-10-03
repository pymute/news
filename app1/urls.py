from django.urls import path
from . import views

urlpatterns = [
    path('', views.pro_list, name='pro_list'),
    path('book/<int:pk>/', views.pro_detail, name='pro_detail'),
    path('book/new/', views.pro_new, name='pro_new'),
    path('book/<int:pk>/edit/', views.pro_edit, name='pro_edit'),
    path('book/<int:pk>/delete/', views.pro_delete, name='pro_delete'),
]
