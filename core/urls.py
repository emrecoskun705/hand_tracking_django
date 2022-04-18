from django.urls import path
from .views import get_ml

app_name = 'core'

urlpatterns = [
    path('get-ml/', get_ml, name='get-ml'),
]
