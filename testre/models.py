from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You might want to use a more secure field like PasswordField
    class Meta:
        app_label = 'testre'


class Loginmodel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    