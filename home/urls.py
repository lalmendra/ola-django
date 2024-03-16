from django.urls import path
from home import views

# namespace para home
app_name = 'home'

# home/
urlpatterns = [
    path('', views.home, name='home'),
]
