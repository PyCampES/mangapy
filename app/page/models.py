from django.conf import settings
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from gcloudauth.models import AuthFileUpload

from google.cloud import vision

# Create your models here.
class Page(models.Model):
    """
    Each image submitted to be processed will be grouped in this model
    """
    image_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    @staticmethod
    def process_uploaded_file(request, file, page):
        credentials = AuthFileUpload.build_credentials_obj(request)
        client = vision.ImageAnnotatorClient(credentials=credentials)

        image_context = vision.ImageContext(language_hints=["ja"])
        image = vision.Image(content=file.read())

        # Performs label detection on the image file
        response = client.text_detection(image=image, image_context=image_context)

        sentences_to_create = []

        for block in response.full_text_annotation.pages[0].blocks:
            block_text = ""
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    block_text += "".join([symbol.text for symbol in word.symbols])
                    latest_vertices = word.bounding_box.vertices[0] #latest_vertices.x , latest_vertices.y

            sentences_to_create.append(
                SentenceBlock(
                        page=page,
                        ocr_text=block_text,
                        position_x=latest_vertices.x,
                        position_y=latest_vertices.y
                    )
            )

        SentenceBlock.objects.bulk_create(sentences_to_create, batch_size=100)

    def delete_related_sentence_blocks(self):
        SentenceBlock.objects.filter(page=self).delete()

class SentenceBlock(models.Model):
    """
    Represents a single sentence and tracks the X, Y position where its found on the image
    """
    page = models.ForeignKey(
        Page,
        related_name="sentences",
        on_delete=models.CASCADE,
    )
    ocr_text = models.CharField(max_length=1000)
    position_x = models.IntegerField()
    position_y = models.IntegerField()