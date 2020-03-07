import json

from django.test import TestCase, Client

from pokemon.models import Pokemon, Attack

TEST_CONTENT = [
    {
        'name': 'Charmander',
        'stage': 'Basic',
        'evolves_from': None,
        'hit_points': 50,
        'energy_type': 'fire',
        'attacks': [
            {
                'name': 'Scratch',
                'energy_required': 1,
                'damage': 10
            },
            {
                'name': 'Ember',
                'energy_required': 2,
                'damage': 30
            }
        ]
    },
    {
        'name': 'Charmeleon',
        'stage': '1',
        'evolves_from': 'Charmander',
        'hit_points': 80,
        'energy_type': 'fire',
        'attacks': [
            {
                'name': 'Flamethrower',
                'energy_required': 3,
                'damage': 80
            }
        ]
    },
    {
        'name': 'Charizard',
        'stage': '2',
        'evolves_from': 'Charmeleon',
        'hit_points': 150,
        'energy_type': 'fire',
        'attacks': [
            {
                'name': 'Fire Spin',
                'energy_required': 4,
                'damage': 200
            }
        ]
    }
]


class PokemonEndpointTestCase(TestCase):

    def test_get(self):
        """
        Test that we can get a list of Pokémon
        """
        client = Client()
        charmander = Pokemon.objects.create(name='Charmander', stage='Basic',
            evolves_from=None, hit_points=50, energy_type='fire')
        scratch = Attack.objects.create(pokemon=charmander,
            name='Scratch', energy_required=1, damage=10)
        ember = Attack.objects.create(pokemon=charmander,
            name='Ember', energy_required=2, damage=30)
        charmeleon = Pokemon.objects.create(name='Charmeleon', stage='1',
            evolves_from=charmander, hit_points=80, energy_type='fire')
        flamethrower = Attack.objects.create(pokemon=charmeleon,
            name='Flamethrower', energy_required=3, damage=80)
        charizard = Pokemon.objects.create(name='Charizard', stage='2',
            evolves_from=charmeleon, hit_points=150, energy_type='fire')
        fire_spin = Attack.objects.create(pokemon=charizard,
            name='Fire Spin', energy_required=4, damage=200)

        response = client.get('/pokemon/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), TEST_CONTENT)