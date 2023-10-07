from django.urls import path
from .views import CaloriesFormView, AboutMe

urlpatterns = [
    path('', CaloriesFormView.as_view(), name='main'),
    path('about-me', AboutMe.as_view(), name='about-me')
]