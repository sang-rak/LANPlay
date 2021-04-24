from django.urls import path
from . import views

app_name = 'meets'
urlpatterns = [
    path('<int:meet_id>/', views.meet, name='meet'),
    path('detectme/', views.detectme, name="detectme"),
]
