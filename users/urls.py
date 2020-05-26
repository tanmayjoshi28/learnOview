from django.conf.urls import url
from .views import Login, Register
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    url(r'^login/$', Login, name='login'),
    url(r'^register/$', Register, name='register'),
]