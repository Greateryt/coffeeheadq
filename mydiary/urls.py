from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_list,name='diary_list'),
    path('create/', views.diary_create,name='diary_create'),
    path('<int:diary_id>/edit/', views.diary_edit,name='diary_edit'),
    path('<int:diary_id>/delete/', views.diary_delete,name='diary_delete'),
    path('register/', views.register,name='register'),
]
