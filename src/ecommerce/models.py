from django.conf import settings
from django.db import models
from .validators import validate_blocked_words
from django.utils.text import slugify
from django.db.models.signals import pre_save
from base.models import BasePublishModel

user = settings.AUTH_USER_MODEL
# Create your models here.
class ProductModel(BasePublishModel):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    descripcion = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, db_index=True)
    user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return f'/product/{self.slug}/'

    def save(self, *args, **kwargs):
        validate_blocked_words(self.title)
        validate_blocked_words(self.descripcion)
        super().save(*args, **kwargs)

def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None or instance.slug == "":
        new_slug = slugify(instance.title)
        my_model = instance.__class__
        qs = my_model.objects.filter(slug__startswith=new_slug).exclude(pk=instance.pk)
        if qs.count() == 0:
            instance.slug = new_slug
        else:
            instance.slug = f"{new_slug}-{qs.count()}"

pre_save.connect(slugify_pre_save, sender=ProductModel) 
        