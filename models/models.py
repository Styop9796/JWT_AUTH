from django.db import models

# Create your models here.
from django.db import models
import secrets

class APIKey(models.Model):
    key = models.CharField(max_length=255, unique=True, default=secrets.token_urlsafe)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='api_keys')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
