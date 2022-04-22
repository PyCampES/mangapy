import io
import json

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from google.oauth2 import service_account


# Create your models here.
class AuthFileUpload(models.Model):
    file = models.FileField(upload_to=settings.UPLOAD_DIR)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def build_credentials_obj(cls, request):
        service_account_file = cls.objects.filter(owner=request.user).first()
        if service_account_file:
            with io.open(service_account_file.file.path) as f:
                json_acct_info = json.load(f)
            return service_account.Credentials.from_service_account_info(
                json_acct_info
            )

