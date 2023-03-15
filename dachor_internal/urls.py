from django.urls import path

from . import views

app_name = 'internal'

urlpatterns = [
    path('', views.StartView.as_view(), name='start'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('not-confirmed/', views.NotConfirmedView.as_view(), name='not-confirmed'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
]
