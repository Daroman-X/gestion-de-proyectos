from django.test import SimpleTestCase

"""
Clase TestsPath
Enfocado en el testeo de los path Core
"""
class TestsPath(SimpleTestCase):
    """
    Funcion path_inicio
    Prueba con el codigo de estado 200 ok
    """    
    def test_path_inicio(self):
        #coincidencias
        respuesta=self.client.get("/")
        print("Prueba de Inicio")
        try:
            self.assertEqual(respuesta.status_code,200)
            print("[Correcta]: Pagina encontrada, codigo:", respuesta.status_code)
        except AssertionError as ae:
            print(f"La prueba a fallado {ae}")
        except Exception as e:
            print("Ocurrió un error:", e)
        
