from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('login/', LoginAccount.as_view(), name='login'),
    path('register/', RegisterAccount.as_view(), name='register'),
    path('add_supp/', add_supplier, name='add_supplier'),
]
