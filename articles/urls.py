from django.urls import path
from .views import makaleler_view

urlpatterns = [
    path('', makaleler_view, name="makaleler-anasayfa")
]