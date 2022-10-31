from django.urls import path, include

from . import views

app_name = 'website'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.HomepageView.as_view(), name='homepage'),
    path('ueber_uns/', views.AboutView.as_view(), name='about'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    path('auftritte/', views.EventsView.as_view(), name='events'),
    path('impressum/', views.ContactView.as_view(), name='impress'),
    path('datenschutz/', views.PrivacyView.as_view(), name='privacy'),
]
