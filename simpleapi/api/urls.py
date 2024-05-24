from django.urls import path
from .views import simple_get_request

urlpatterns = [
    path('', simple_get_request, name='simple_get_api'),
]
