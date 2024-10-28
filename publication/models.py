from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=255, null=False)
    text_publication = models.TextField()

    def __str__(self):
        return self.title