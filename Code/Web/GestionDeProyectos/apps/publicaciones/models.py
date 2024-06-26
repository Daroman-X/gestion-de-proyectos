from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Publicacion(models.Model):
    titulo=models.CharField(max_length=255)
    texto=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    autor=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    
    def __str__(self):
        return self.titulo[:50]
    
    def get_absolute_url(self):
        return reverse("publicacion:detalle",args=[str(self.id)])
    
class Comentario(models.Model):
    publicacion=models.ForeignKey(Publicacion,on_delete=models.CASCADE, related_name="comentarios")
    comentario=models.CharField(max_length=255)
    autor=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse("publicacion:inicio")
    