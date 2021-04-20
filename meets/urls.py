from django.urls import path
from . import views

app_name = 'meets'
urlpatterns = [
    path('<int:room_id>', views.meet, name='meet')
]
