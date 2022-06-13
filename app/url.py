from django.urls import path
from.views import personaList

urlpatterns = [
    path('persona/',personaList.as_view(),name='persona_list')
]