from django.test import TestCase
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
import json

class HomeViewTestCase(TestCase):
    def setUp(self):
        # Crear un cliente de pruebas y un usuario de prueba
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', first_name='John', password='testpassword')

    @patch('requests.get')
    def test_home_view_authenticated_user(self, mock_get):
        """Prueba que la vista 'home_view' responde correctamente para un usuario autenticado."""
        
        # Simular la respuesta de la API de OpenWeatherMap
        mock_response = {
            "weather": [{"icon": "10d"}],
            "main": {"temp": 25, "humidity": 70},
            "sys": {"country": "CO"}
        }
        mock_get.return_value.json.return_value = mock_response

        # Iniciar sesión como el usuario de prueba
        self.client.login(username='testuser', password='testpassword')

        # Hacer la solicitud GET a la vista
        response = self.client.get(reverse('home'))

        # Verificar que la respuesta tenga un código de estado 200
        self.assertEqual(response.status_code, 200)

        # Verificar que el saludo personalizado se muestra en el contexto
        self.assertIn('greet', response.context)
        self.assertTrue(response.context['greet'].startswith('Hello John, '))

        # Verificar que la cita del día está en el contexto
        self.assertIn('quote', response.context)

        # Verificar que la respuesta de la API se incluye en el contexto
        self.assertEqual(response.context['temp'], 25)
        self.assertEqual(response.context['country'], 'CO')
        self.assertEqual(response.context['icon'], '10d')

    def test_home_view_unauthenticated_user(self):
        """Prueba que la vista 'home_view' responde correctamente para un usuario no autenticado."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['greet'].startswith('Hello, '))
