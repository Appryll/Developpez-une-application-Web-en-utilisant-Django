from django.db import models
from django.conf import settings
from PIL import Image

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tickets")
    image = models.ImageField(null=True, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (600, 600)

    if image is True:
        def resize_image(self):
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            self.resize_image()

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return f'{self.title}'
