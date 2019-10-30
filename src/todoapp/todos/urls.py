from django.urls import path

from .views import HomePageView, LogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('logout', LogoutView.as_view(), name='logout')
]