from django.db import models
from django.conf import settings


class Announcement(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="announcements",
    )

    text = models.CharField(max_length=250, default= "sample text")


    def __str__(self):
        return f"{self.author}: {self.text[:50]}"