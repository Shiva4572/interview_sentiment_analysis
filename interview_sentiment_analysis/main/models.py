from django.db import models

# Create your models here.

class admin(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password = models.CharField(max_length=45)
    email=models.CharField(max_length=45)

class audio(models.Model):
    audio = models.FileField(upload_to="documents/")
    class Meta:
        db_table='Audio_store'