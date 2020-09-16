from django.conf import settings
from django.db import models
from django.utils import timezone

class Records(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    def __str__(self):
        return self.user.username