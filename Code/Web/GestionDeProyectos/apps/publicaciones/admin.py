from django.contrib import admin
from .models import Publicacion,Comentario

class ComentarioInline(admin.StackedInline):
    model=Comentario
    extra=0
    
class PublicacionAdmin(admin.ModelAdmin):
    inlines=[
        ComentarioInline
    ]

admin.site.register(Publicacion,PublicacionAdmin)
admin.site.register(Comentario)