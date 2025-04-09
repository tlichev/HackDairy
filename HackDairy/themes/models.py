from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Theme(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='themes')
    banner_image = models.ImageField(upload_to='theme_banners', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

