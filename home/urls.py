from django.urls import path
from .views import register_user, login_user, create_order, dashboard_stats, api_home

urlpatterns = [
    path('', api_home, name='api_home'),  # یہ لائن اب خالی پاتھ کا ایرر ختم کر دے گی
    path('api/register/', register_user, name='register_user'),
    path('api/login/', login_user, name='login_user'),
    path('api/create-order/', create_order, name='create_order'),
    path('api/dashboard-stats/', dashboard_stats, name='dashboard_stats'),
]