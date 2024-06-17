from locust import HttpUser, task

class MyUser(HttpUser):
    @task(weight=1)
    def visit_inicio(self):
        self.client.get("/")

    @task(weight=2)
    def visit_gestion(self):
        self.client.get("/gestion/")

    @task(weight=3)
    def visit_formatos(self):
        self.client.get("/formatos/")

    @task(weight=4)
    def visit_tablero(self):
        self.client.get("/tablero/")