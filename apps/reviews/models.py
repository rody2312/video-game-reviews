from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    