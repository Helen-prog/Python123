from django.urls import path
from .views import weather, deletecity

urlpatterns = [
    path('', weather, name='weather'),
    path('<int:city_pk>', deletecity, name='deletecity')
]
