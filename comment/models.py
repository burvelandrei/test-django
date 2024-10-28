from django.db import models
from publication.models import Publication

# Create your models here.
class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return f"Comment on {self.publication.title}"