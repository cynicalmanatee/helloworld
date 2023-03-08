# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, harryPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('harry/', harryPageView, name='harry'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),

]
