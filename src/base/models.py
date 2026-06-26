from django.db import models
from django.utils import timezone



# Create your models here.
class BasePublishModel(models.Model):
    class ProductStateChoices(models.TextChoices):
        PUBLISHED = "PU", "Publicado"
        DRAFT = "DR", "Borrador"
        PRIVATE = "PR", "Privado"

    state = models.CharField(max_length=2, choices=ProductStateChoices.choices, default=ProductStateChoices.DRAFT)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    published_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)


    class Meta:
        abstract = True
        ordering = ["-updated", "-timestamp"]

    def save(self, *args, **kwargs):
        if self.state_is_published and self.published_timestamp is None:
            self.published_timestamp = timezone.now()
        else:
            self.published_timestamp = None
        super().save(*args, **kwargs)
    
    @property
    def state_is_published(self):
        return self.state == self.ProductStateChoices.PUBLISHED

    def is_published(self):
        publish_timestamp = self.published_timestamp
        return self.state_is_published and publish_timestamp < timezone.now()