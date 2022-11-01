from django.urls import path

from . import views

app_name = 'internal'

urlpatterns = [
    path('', views.StartView.as_view(), name='start'),
]
