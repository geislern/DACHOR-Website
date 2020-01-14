from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('ueber_uns/', views.AboutView.as_view(), name='about'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    path('auftritte/', views.EventsView.as_view(), name='events'),
    path('impressum/', views.ImpressView.as_view(), name='impress'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('datenschutz/', views.PrivacyView.as_view(), name='privacy'),
]
