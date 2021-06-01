from django.urls import path
from .views import registro_retirada_create


urlpatterns = [
    path('create/', registro_retirada_create, name="registro_retirada_create"),
]