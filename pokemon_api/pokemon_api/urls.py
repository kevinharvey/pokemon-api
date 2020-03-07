from django.contrib import admin
from django.urls import path

from rest_framework import routers

from pokemon.views import PokemonViewSet


router = routers.DefaultRouter()
router.register(r'pokemon', PokemonViewSet)

urlpatterns = router.urls + [
    path('admin/', admin.site.urls),
]
