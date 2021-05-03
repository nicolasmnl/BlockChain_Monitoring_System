from django.urls import path
from .views import block_list
from .views import block_create
from .views import block_view



urlpatterns = [
    path('list/', block_list, name="block_list"),
    path('create/', block_create, name="block_create"),
    path('view/<str:hashcode>', block_view, name="block_view"),
    # path('add/', block_add, name="block_add"),
]