from django import forms

from page.models import Page


class PageUploadForm(forms.ModelForm):

    file = forms.FileField(required=False)

    class Meta:
        model = Page
        exclude = ('image_name', 'owner', )

