from django.contrib import admin
from gcloudauth.forms import AuthFileUploadForm
from gcloudauth.models import AuthFileUpload



class AuthFileUploadAdmin(admin.ModelAdmin):
    form = AuthFileUploadForm
    list_display = ('file', 'owner', )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(AuthFileUpload, AuthFileUploadAdmin)