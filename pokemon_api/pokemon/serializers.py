from rest_framework import serializers

from .models import Pokemon, Attack


class AttackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attack
        fields = ('name', 'energy_required', 'damage',)


class PokemonSerializer(serializers.ModelSerializer):
    evolves_from = serializers.SerializerMethodField()
    attacks = AttackSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = ('name', 'stage', 'evolves_from', 'hit_points', 
            'energy_type', 'attacks',)

    def get_evolves_from(self, obj):
        return obj.evolves_from.name if obj.evolves_from else None
