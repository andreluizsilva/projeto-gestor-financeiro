from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
