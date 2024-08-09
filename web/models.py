
import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField()
    imagen_url = models.URLField()
    slug = models.SlugField()
    precio = models.FloatField(default=10990)
    es_privado = models.BooleanField()



class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField()
    name = models.CharField(max_length=64)
    message = models.TextField()

class Suscription(models.Model):
    email = models.EmailField(unique=True)
    date_suscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
