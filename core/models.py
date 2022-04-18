from django.db import models


class MLModel(models.Model):
    data = models.CharField(max_length=1000)
