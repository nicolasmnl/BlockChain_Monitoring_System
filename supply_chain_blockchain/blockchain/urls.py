from django.urls import path
from .views import block_list
from .views import block_create




urlpatterns = [
    path('list/', block_list, name="block_list"),
    path('create/', block_create, name="block_create"),

]