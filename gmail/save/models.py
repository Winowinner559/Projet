from django.db import models

class UserCredentials(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)  # Le mot de passe doit être haché pour la sécurité

    def __str__(self):
        return self.email
