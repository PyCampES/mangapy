from django import forms
from gcloudauth.models import AuthFileUpload

class AuthFileUploadForm(forms.ModelForm):

    class Meta:
        model = AuthFileUpload
        exclude = ('owner', )