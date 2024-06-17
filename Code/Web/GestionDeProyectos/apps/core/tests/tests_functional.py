from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PruebasFuncionales(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)  # Espera implícita para todos los elementos

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_pagina_inicio(self):
        # Navegar a la página de inicio
        self.driver.get(self.live_server_url)
        self.assertIn("Inicio", self.driver.title)  # Ajusta esto según el título de tu página de inicio

    def test_pagina_gestion(self):
        # Construir la URL completa para la ruta 'gestion/'
        gestion_url = f"{self.live_server_url}/gestion/"
        self.driver.get(gestion_url)

        try:
            # Verificar que un elemento específico esté presente en la página de gestión
            elemento = self.driver.find_element(By.ID, 'id_del_elemento')  # Ajusta esto según tu HTML
            self.assertIsNotNone(elemento)
        except NoSuchElementException:
            self.fail("El elemento esperado no se encontró en la página de gestión")

# Ejecutar las pruebas
if __name__ == "__main__":
    import unittest
    unittest.main()
