from django.urls import path
from . import views


app_name = 'rooms'
urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('<int:user_id>/', views.profile, name='profile'),
    # path('<int:user_id>/follow/', views.follow, name='follow'),
]