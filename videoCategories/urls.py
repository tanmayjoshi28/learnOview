from django.conf.urls import url
from . import views

app_name = 'videoCategories'

urlpatterns = [
    url(r'^homepage/$', views.homePage, name='homepage'),
]



