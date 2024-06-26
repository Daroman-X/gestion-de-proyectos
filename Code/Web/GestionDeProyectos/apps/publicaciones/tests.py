from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Publicacion


class PublicacionViewTest(TestCase):
    
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username="daro_test",
            email="darotest@gmail.com",
            password="1234"
        )
        
        self.publicacion=Publicacion.objects.create(
            titulo="Titulo de prueba",
            texto="Texto de prueba",
            autor=self.user,
        )
        
    def test_contenido(self):
        self.assertEqual(f'{self.publicacion.titulo}', 'Titulo de prueba')
        self.assertEqual(f'{self.publicacion.texto}', 'Texto de prueba')
        self.assertEqual(f'{self.publicacion.autor}', 'daro_test')
        
    def test_detalle(self):
        url = reverse('publicacion:detalle', args=[self.publicacion.id])
        respuesta = self.client.get(url)
        no_encontrada = self.client.get(reverse('publicacion:detalle', args=[1000]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(no_encontrada.status_code, 404)


class PublicacionPathTest(TestCase):
    """
    Clase para probar la configuración de la aplicación de Publicación.

    Esta clase verifica los siguientes aspectos de la configuración de la aplicación:
    
    - path: Asegura que los paths estén correctamente definidos.
    - nombre del path: Verifica que los nombres de los paths sean correctos.
    - template del path: Revisa que los templates asociados a cada path existan y sean accesibles.

    Atributos:
    ----------
    paths (list): Lista de tuples que contienen la información de los paths (path, nombre, template).

    Métodos:
    --------
    revisar_paths():
        Revisa que todos los paths estén correctamente definidos.

    revisar_nombres():
        Verifica que todos los nombres de los paths sean correctos y únicos.

    revisar_templates():
        Asegura que todos los templates asociados a los paths existan.
    """
            
    def test_url_existe(self):
        respuesta=self.client.get("/publicaciones/")
        self.assertEqual(respuesta.status_code,200)
        
    def test_url_nombre(self):
        respuesta=self.client.get(reverse("publicacion:inicio"))
        self.assertEqual(respuesta.status_code,200)
        
    def test_template_existe(self):
        respuesta=self.client.get(reverse("publicacion:inicio"))
        self.assertEqual(respuesta.status_code,200)
        self.assertTemplateUsed(respuesta,"publicacion/index.html")
        
