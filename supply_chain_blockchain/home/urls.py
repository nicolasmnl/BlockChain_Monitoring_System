from django.urls import path
from .views import home, log_out


urlpatterns = [
    path('', home, name='home'),
    path('logout/', log_out, name='log_out')

]