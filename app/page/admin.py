from django.contrib import admin
from page.forms import PageUploadForm

from page.models import Page, SentenceBlock

# Register your models here.
class SentenceBlockInline(admin.TabularInline):
    model = SentenceBlock


class PageAdmin(admin.ModelAdmin):
    inlines = [
        SentenceBlockInline,
    ]

    form = PageUploadForm

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        breakpoint()
        uploaded_file = request.FILES.get('file')

        if change and uploaded_file:
            self.model.delete_related_sentence_blocks(obj)

        if not uploaded_file:
            return None

        obj.image_name = uploaded_file._name
        obj.owner = request.user
        super().save_model(request, obj, form, change)
        Page.process_uploaded_file(request, uploaded_file, obj)

        return obj



    class Meta:
        model = Page
        exclude = ('owner', )


admin.site.register(Page, PageAdmin)