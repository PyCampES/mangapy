from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class AuthFileUpload(models.Model):
    file = models.FileField(upload_to=settings.UPLOAD_DIR)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)