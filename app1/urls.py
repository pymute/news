from django.urls import path
from . import views

urlpatterns = [
    path('', views.pro_list, name='pro_list'),
    path('detail/<int:pk>/', views.pro_list, name='pro_detail'),
    path('pro_new/<int:id>/', views.pro_new, name='pro_new'),
    path('update/<int:pk>/edit/', views.pro_edit, name='pro_edit'),
    path('delete/<int:pk>/', views.pro_delete, name='pro_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
