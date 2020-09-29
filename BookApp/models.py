from django.db import models

from django.utils.text import slugify


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    media = models.ImageField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
