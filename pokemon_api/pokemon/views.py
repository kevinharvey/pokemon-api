from rest_framework import viewsets

from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer


class PokemonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
