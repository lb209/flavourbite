from django.urls import path
from home import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    path('home/', views.read, name='read'),

    path('create/', views.create_update, name='create'),
    path('edit/<int:id>/', views.create_update, name='edit'),

    path('profile/<int:id>/', views.profile_view, name='profile'),

    path('delete/<int:id>/', views.delete, name='delete'),
]